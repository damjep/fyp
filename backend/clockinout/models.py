from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from shifts.models import Shift

User = get_user_model()

class ClockInOut(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    clock_in_time = models.DateTimeField(null=True, blank=True)
    clock_out_time = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)

    total_tips = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        unique_together = ('user', 'shift', 'date')

    def __str__(self):
        return f"{self.user.name} - {self.shift} - {self.date} - In: {self.clock_in_time} Out: {self.clock_out_time}"

    def clock_in(self):
        if self.clock_in_time is not None:
            raise ValueError("Already clocked in.")
        self.clock_in_time = timezone.now()
        self.save(update_fields=['clock_in_time'])

    def clock_out(self):
        if self.clock_in_time is None:
            raise ValueError("Must clock in before clocking out.")
        if self.clock_out_time is not None:
            raise ValueError("Already clocked out.")
        self.clock_out_time = timezone.now()
        self.is_completed = True
        self.save(update_fields=['clock_out_time', 'is_completed'])
        self.calculate_tips_and_service_charge()

    def calculate_tips_and_service_charge(self):
        """Calculate total tips and service charge for this clocked shift."""
        from posFin.models import Payment  # Adjust if Payment model is elsewhere

        if not self.clock_in_time or not self.clock_out_time:
            # Skip if incomplete
            return

        # Get payments made between clock in and out time
        payments = Payment.objects.filter(
            timestamp__gte=self.clock_in_time,
            timestamp__lte=self.clock_out_time,
            order__status='paid'
        )

        totals = payments.aggregate(
            total_tips=models.Sum('order__tips'),
            total_service_charge=models.Sum('order__service_charge')
        )

        self.total_tips = totals['total_tips'] or 0
        self.total_service_charge = totals['total_service_charge'] or 0
        self.save(update_fields=['total_tips', 'total_service_charge'])
