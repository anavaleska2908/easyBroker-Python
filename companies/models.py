import uuid
from django.db import models


class Company(models.Model):
    class Meta:
        db_table = "tbl_companies"
        
    id = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )
    dba  = models.CharField(
        db_column = "cpy_dba",
        max_length=255
    )
    corporate_name = models.CharField(
        db_column = "cpy_corporate_name",
        max_length=255
    )
    municipal_registration = models.CharField(
        db_column = "cpy_municipal_registration",
        max_length=14
    )
    state_registration = models.CharField(
        db_column = "cpy_state_registration",
        max_length=14
    )
    email = models.EmailField(
        db_column = "cpy_email",
        max_length=255
    )
    phone = models.CharField(
        db_column = "cpy_phone",
        max_length=11
    )
    cnpj = models.CharField(
        db_column = "cpy_cnpj",
        unique = True,
        max_length = 14
    )
    created_at = models.DateTimeField(
        auto_now_add= True,
        db_column = "cpy_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        db_column = "cpy_updated_at"
    )