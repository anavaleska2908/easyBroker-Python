from rest_framework.serializers import ModelSerializer
from occupations.models import Occupation


class OccupationSerializer(ModelSerializer):

    class Meta:
        model = Occupation
        fields = [
            "id",
            "name",
            "company",
            "created_at",
            "updated_at"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
            "company": {"write_only": True}
        }
