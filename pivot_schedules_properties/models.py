from django.db import models
import uuid


class PivotSchedulesProperties(models.Model):
    class Meta:
        db_table = "tbl_pivot_schedules_properties"

    id = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )
    schedule = models.ForeignKey(
        "schedules.Schedule",
        db_column = "puc_id_schedule_fk",
        on_delete = models.SET_NULL,
        null = True,
        default = None
    )
    property = models.ForeignKey(
        "properties.Property",
        db_column = "puc_id_property_fk",
        on_delete = models.SET_NULL,
        null = True,
        default = None
    )
    created_at = models.DateTimeField(
        db_column = "puc_created_at",
        auto_now_add = True
    )
    updated_at = models.DateTimeField(
        db_column = "puc_updated_at",
        auto_now = True
    )