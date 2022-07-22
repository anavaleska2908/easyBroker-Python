import uuid
from django.db import models


class Address(models.Model):
    class Meta:
        db_table = "tbl_addresses"

    id = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )

    uf = models.CharField(
        db_column = "ads_uf",
        max_length = 2,
    )
    
    city = models.CharField(
        db_column = "ads_city",
        max_length = 255,
    )

    neighborhood = models.CharField(
        db_column = "ads_neighborhood",
        max_length = 255,
    )

    street = models.CharField(
        db_column = "ads_street",
        max_length = 255,
    )

    complement = models.CharField(
        db_column = "ads_complement",
        max_length = 50,
    )

    number = models.CharField(
        db_column = "ads_number",
        max_length = 10,
    )

    cep = models.CharField(
        db_column = "ads_cep",
        max_length = 14,
    )

    user = models.ForeignKey(
        "users.User",
        on_delete = models.SET_NULL,
        null = True,
        default = None,
        db_column = "ads_user",
    )

    company = models.ForeignKey(
        "companies.Company",
        on_delete = models.SET_NULL,
        null = True,
        default = None,
        db_column = "ads_company",
    )

    property = models.ForeignKey(
        "properties.Property",
        on_delete = models.SET_NULL,
        null = True,
        default = None,
        db_column = "ads_property",
    )

    created_at = models.DateTimeField(
        auto_now_add= True,
        db_column = "ads_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        db_column = "ads_updated_at"
    )