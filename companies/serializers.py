from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from addresses.serializers import AddressSerializer
from companies.models import Company
from addresses.models import Address
from users.models import User
from users.serializers import UserSerializer
from pivot_users_companies.models import PivotUsersCompanies



class CompanySerializer(ModelSerializer):
    address = AddressSerializer(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Company
        fields = [
            "id",
            "dba",
            "corporate_name",
            "municipal_registration",
            "state_registration",
            "email",
            "phone",
            "cnpj",
            "user",
            "address",
            "created_at",
            "updated_at"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "user": {"write_only": True},
            "address": {"write_only": True},
        }

    def create(self, validated_data):
        company, user, address = self._validate_data(validated_data)
        new_company = self._create_company(company)
        new_user = self._create_user(user)
        self._link_company(new_user, new_company)
        self._create_and_link_addres(address, new_company)
        return new_company

    @staticmethod
    def _validate_data(data):
       address = data.pop("address", None)
       user = data.pop("user", None)
       return data, user, address

    @staticmethod
    def _create_company(data):
        return Company.objects.create(**data)

    @staticmethod
    def _create_user(data):
       return User.objects.create_superuser(**data)

    @staticmethod
    def _create_and_link_addres(address, company):
        if (address and company):
            Address.objects.create(**address, company=company)

    @staticmethod
    def _link_company(user, company):
        if(user):
            PivotUsersCompanies.objects.create(user=user, company = company)
    
 