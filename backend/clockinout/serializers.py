from rest_framework import serializers
from .models import ClockInOut

class ClockInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClockInOut
        fields = ['id', 'user', 'shift', 'date', 'clock_in_time', 'clock_out_time', 'is_completed']

class ClockInOutSummarySerializer(serializers.ModelSerializer):
    shift_name = serializers.SerializerMethodField()

    class Meta:
        model = ClockInOut
        fields = [
            'id',
            'date',
            'shift_name',
            'clock_in_time',
            'clock_out_time',
            'total_tips',
            'total_service_charge',
        ]

    def get_shift_name(self, obj):
        return f"{obj.shift.days} {obj.shift.shift_type} from {obj.shift.shift_start}:00 to {obj.shift.shift_end}:00"
