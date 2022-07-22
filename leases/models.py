import uuid
from django.db import models


class Lease(models.Model):
    class Meta:
        db_table = "tbl_leases"

    id = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )
    user = models.ForeignKey(
        "users.user",
        db_column = "lse_id_user_fk",
        on_delete = models.SET_NULL,
        null = True,
        default = None,
    )
    company = models.ForeignKey(
        "companies.Company",
        db_column = "lse_id_company_fk",
        on_delete = models.SET_NULL,
        null = True,
        default = None,
    )
    property = models.ForeignKey(
        "properties.Property",
        db_column = "lse_id_property_fk",
        on_delete = models.SET_NULL,
        null = True,
        default = None,
    )
    property_value = models.FloatField(
        db_column = "lse_property_value",
        default = 0
    )
    created_at = models.DateTimeField(
        db_column = "lse_created_at",
        auto_now_add= True
    )
    updated_at = models.DateTimeField(
        db_column = "lse_updated_at",
        auto_now= True
    )