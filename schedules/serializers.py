from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from schedules.models import Schedule
from properties.models import Property
from pivot_schedules_properties.models import PivotSchedulesProperties


class ScheduleSerializer(ModelSerializer, Serializer):
    properties_list = serializers.ListField(required=False)

    class Meta:
        model = Schedule
        fields = [
            "id",
            "comments",
            "status_schedule",
            "start_time",
            "end_time",
            "client",
            "broker",
            "company",
            "properties_list",
            "created_at",
            "updated_at"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "client": {"write_only": True},
            "broker": {"write_only": True},
            "company": {"write_only": True},
            "properties_list": {"write_only": True},
        }
    def create(self, validated_data):
        properties_list = validated_data.pop("properties_list", None)
        schedule = Schedule.objects.create(**validated_data)
        for property_id in properties_list:
            property = Property.objects.get(pk=property_id)
            PivotSchedulesProperties.objects.create(schedule=schedule, property=property)
        
        return schedule
             