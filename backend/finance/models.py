from django.db import models
from posFin.models import Payment

class FinanceReport(models.Model):
    date = models.DateField(unique=True)
    total_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_tips = models.DecimalField(max_digits=10, decimal_places=2 , default=0)
    total_service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    @classmethod
    def updateFinancialReport(cls):
        from django.utils.timezone import now
        from django.db.models import Sum
        
        today = now().date()
        totals = Payment.objects.filter(timestamp__date=today).aggregate(
            total_sales = Sum('amount_paid'),
            total_tips = Sum('order__tips'),
            total_service_charge = Sum('order__service_charge')
        )
        total_sales = totals["total_sales"] if totals["total_sales"] is not None else 0
        total_tips = totals["total_tips"] if totals["total_tips"] is not None else 0
        total_service_charge = totals["total_service_charge"] if totals["total_service_charge"] is not None else 0

        # Update or create the record
        record, created = cls.objects.get_or_create(
            date=today,
            defaults={
                "total_sales": total_sales,
                "total_tips": total_tips,
                "total_service_charge": total_service_charge,
            }
        )
        
        # If the record already exists, update it
        if not created:
            record.total_sales = total_sales
            record.total_tips = total_tips
            record.total_service_charge = total_service_charge
            record.save()
    
    def __str__(self):
        return f"{self.date} - Total Sales: {self.total_sales}"