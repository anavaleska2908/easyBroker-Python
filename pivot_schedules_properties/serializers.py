from rest_framework.serializers import ModelSerializer
from users.models import User


class PivotSchedulesPropertiesSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id","schedule","property"]
        extra_kwargs = {
            "id": {"read_only": True},
            "schedule": {"write_only": True},
            "property": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
