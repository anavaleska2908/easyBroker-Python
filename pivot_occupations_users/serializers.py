from rest_framework.serializers import ModelSerializer
from pivot_occupations_users.models import PivotOccupationsUsers


class PivotOccupationsUsersSerializer(ModelSerializer):

    class Meta:
        model = PivotOccupationsUsers
        fields = [
            "id",
            "occupation",
            "user",
            "created_at",
            "updated_at"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }
