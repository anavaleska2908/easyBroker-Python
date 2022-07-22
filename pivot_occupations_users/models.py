import uuid
from django.db import models


class PivotOccupationsUsers(models.Model):
    class Meta:
        db_table = "tbl_pivot_occupations_users"

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    occupation = models.ForeignKey(
        "occupations.Occupation",
        db_column="pou_id_occupation_fk",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    user = models.ForeignKey(
        "users.User",
        db_column="pou_id_user_fk",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column="pou_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_column="pou_updated_at"
    )
