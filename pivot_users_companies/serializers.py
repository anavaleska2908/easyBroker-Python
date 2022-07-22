from rest_framework.serializers import ModelSerializer
from users.models import User


class PivotUsersCompaniesSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id","user","company","created_at","updated_at"]
        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"write_only": True},
            "company": {"write_only": True},
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True}
        }
