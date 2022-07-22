import uuid
from django.db import models


class Property(models.Model):
    class Meta:
        db_table = "tbl_properties"
        
    id = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )
    property_registration = models.CharField(
        db_column = "pty_property_registration",
        max_length= 14,
        unique=True
    )
    description = models.TextField(
        db_column = "pty_description",
        null= True,
        default = None
    )
    status_situation = models.SmallIntegerField(
        db_column = "pty_status_situation",
        default = 1
    )
    status_condominium = models.SmallIntegerField(
        db_column = "pty_status_condominium",
        default = 0
    )
    status_service = models.SmallIntegerField(
        db_column = "pty_status_service",
        default = 0
    )
    status_type = models.SmallIntegerField(
        db_column = "pty_status_type",
        default = 1
    )
    status_garage = models.SmallIntegerField(
        db_column = "pty_status_garage",
        default = 3
    )
    qty_bedrooms = models.SmallIntegerField(
        db_column = "pty_qty_bedrooms",
        default = 1
    )
    qty_suites = models.SmallIntegerField(
        db_column = "pty_qty_suites",
        default = 0
    )
    qty_garage_vacancies = models.SmallIntegerField(
        db_column = "pty_qty_garage_vacancies",
        default = 1
    )
    qty_bathroom = models.SmallIntegerField(
        db_column = "pty_qty_bathroom",
        default = 1
    )
    created_at = models.DateTimeField(
        auto_now_add= True,
        db_column = "pty_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        db_column = "pty_updated_at"
    )