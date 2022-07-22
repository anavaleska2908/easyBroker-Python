import uuid
from django.db import models


class Schedule(models.Model):
    class Meta:
        db_table = "tbl_schedules"

    id = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )
    comments = models.TextField(
        db_column="sch_comments",
    )
    status_schedule = models.SmallIntegerField(
        db_column="sch_status_schedule",
    )
    start_time = models.DateTimeField(
        db_column="sch_start_time",
    )
    end_time = models.DateTimeField(
        db_column="sch_end_time",
    )
    client = models.ForeignKey(
        "users.user",
        db_column = "puc_id_client_fk",
        on_delete = models.SET_NULL,
        null = True,
        default = None,
        related_name = "client"
    )
    broker = models.ForeignKey(
        "users.user",
        db_column = "puc_id_broker_fk",
        on_delete = models.SET_NULL,
        null = True,
        default = None,
        related_name = "broker"
    )
    company = models.ForeignKey(
        "companies.Company",
        db_column = "puc_id_company_fk",
        on_delete = models.SET_NULL,
        null = True,
        default = None
    )
    created_at = models.DateTimeField(
        auto_now_add= True,
        db_column = "sch_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        db_column = "sch_updated_at"
    )