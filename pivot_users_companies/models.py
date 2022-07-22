from django.db import models
import uuid


class PivotUsersCompanies(models.Model):
    class Meta:
        db_table = "tbl_pivot_users_companies"

    id = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )
    user = models.ForeignKey(
        "users.user",
        null = True,
        on_delete = models.SET_NULL,
        default = None,
        db_column = "puc_id_user_fk"
    )
    company = models.ForeignKey(
        "companies.Company",
        null = True,
        on_delete = models.SET_NULL,
        default = None,
        db_column = "puc_id_company_fk"
    )
    created_at = models.DateTimeField(
        auto_now_add = True,
        db_column = "puc_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now = True,
        db_column = "puc_updated_at"
    )