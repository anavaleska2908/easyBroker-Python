import uuid
from django.db import models


class Occupation(models.Model):
    class Meta:
        db_table = "tbl_occupations"

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False
    )
    name = models.CharField(
        db_column="occ_name",
        max_length=255,
    )
    company = models.ForeignKey(
        "companies.Company",
        db_column="occ_id_company_fk",
        on_delete=models.SET_NULL,
        null=True,
        default=None
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_column="occ_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        db_column="occ_updated_at"
    )
