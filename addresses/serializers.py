from rest_framework.serializers import ModelSerializer, Serializer
from addresses.models import Address


class AddressSerializer(ModelSerializer):

    class Meta:
        model = Address
        fields = [
            "id",
            "uf",
            "city",
            "neighborhood",
            "street",
            "complement",
            "number",
            "cep",
            "user",
            "company",
            "property",
            "created_at",
            "updated_at"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "user": {"write_only": True},
            "company": {"write_only": True},
            "property": {"write_only": True}
        }