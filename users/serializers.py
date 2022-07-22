from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework import serializers
from addresses.models import Address
from companies.models import Company
from occupations.models import Occupation
from pivot_occupations_users.models import PivotOccupationsUsers
from users.models import User
from pivot_users_companies.models import PivotUsersCompanies
from addresses.serializers import AddressSerializer
    
class UserSerializer(ModelSerializer,Serializer):
    address = AddressSerializer(required = False)
    company = serializers.CharField(required = False)
    occupations = serializers.ListField(required = False)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "cpf",
            "birthdate",
            "email",
            "password",
            "phone",
            "address",
            "company",
            "occupations",
            "created_at",
            "updated_at"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "cpf": {"write_only": True},
            "password": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }

    def create(self, validated_data):
        user, company, address, occupations = self._validate_data(validated_data)
        new_user = self._create_user(user)
        self._link_company(company, new_user)
        self._link_occupations(occupations, new_user)
        self._create_and_link_address(address, new_user)
        return new_user

    @staticmethod
    def _validate_data(data):
        address = data.pop("address", None)
        company = data.pop("company", None)
        occupations = data.pop("occupations", None)
        return data, company, address, occupations

    @staticmethod
    def _create_user(data):
        return User.objects.create(**data)
            
    @staticmethod
    def _create_and_link_address(address, user):
        if (address): 
            Address.objects.create(**address, user = user)

    @staticmethod
    def _link_occupations(occupations,user):
        if (occupations):
            for occupation_id in occupations:
                occupation = Occupation.objects.get(pk = occupation_id)
                PivotOccupationsUsers.objects.create(user = user, occupation = occupation)
            
    @staticmethod
    def _link_company(company_id,user):
        if (company_id):
            company = Company.objects.get(pk = company_id)
            PivotUsersCompanies.objects.create(user = user, company = company)