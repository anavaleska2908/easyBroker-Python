from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from leases.models import Lease


class LeaseSerializer(ModelSerializer, Serializer):
    # user = serializers.CharField(required = False)
    # company = serializers.CharField(required = False)
    # property = serializers.CharField()

    class Meta:
        model = Lease
        fields = [
            "id",
            "property_value",
            "user",
            "company",
            "property",
            "created_at",
            "updated_at"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"write_only": True},
            "company": {"write_only": True},
            "property": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
