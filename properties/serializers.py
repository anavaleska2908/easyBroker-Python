from rest_framework.serializers import ModelSerializer,Serializer
from rest_framework import serializers
from leases.models import Lease
from addresses.serializers import AddressSerializer
from addresses.models import  Address
from properties.models import Property
from companies.models import Company
from users.models import User


class PropertySerializer(ModelSerializer,Serializer):
    user = serializers.CharField(required = False)
    company = serializers.CharField(required = False)
    address = AddressSerializer(required = False)
    property_value = serializers.DecimalField(required = False, max_digits = 10, decimal_places = 2)


    class Meta:
        model = Property
        fields = [
            "id",
            "user",
            "company",
            "address",
            "property_value",
            "property_registration",
            "description",
            "status_situation",
            "status_condominium",
            "status_service",
            "status_type",
            "status_garage",
            "qty_bedrooms",
            "qty_suites",
            "qty_garage_vacancies",
            "qty_bathroom",
            "created_at",
            "updated_at",
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "user": {"write_only": True},
            "company": {"write_only": True},
            "address": {"write_only": True},
            "property_value": {"write_only": True}
            }

    def create(self, validated_data):
        property, user, company, address, property_value = self._validate_data(validated_data)
        new_property = self._create_property(property)
        self._create_and_link_address(address, new_property)
        self._create_lease(new_property, user, company, property_value)
        return new_property

    @staticmethod
    def _validate_data(data):
        user = data.pop("user", None)
        company = data.pop("company", None)
        address = data.pop("address", None)
        property_value = data.pop("property_value", None)
        return data, user, company, address, property_value

    @staticmethod
    def _create_property(data):
        return Property.objects.create(**data)
            
    @staticmethod
    def _create_and_link_address(address,property):
        if (address and property): 
            Address.objects.create(**address, property = property)

    @staticmethod
    def _create_lease(property, user_id, company_id, property_value):
        if (property and user_id ):
            user = User.objects.get(pk = user_id) if user_id else None
            company = Company.objects.get(pk = company_id) if company_id else None
            Lease.objects.create(
                property = property,
                user = user,
                company = company,
                property_value = property_value
            )