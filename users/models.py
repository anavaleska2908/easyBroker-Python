from django.db import models
from addresses.models import Address
from users.utils import UtilsUser
import uuid
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    is_staff = None
    last_login = None
    date_joined = None
    class Meta:
        db_table = "tbl_users"
  
    id = models.UUIDField(
        default = uuid.uuid4,
        unique = True,
        primary_key = True,
        editable = False
    )
    first_name = models.CharField(
        db_column = "usr_first_name",
        max_length = 255
    )
    last_name = models.CharField(
        db_column = "usr_last_name",
        max_length = 255
    )
    birthdate = models.DateField(
        db_column = "usr_birthdate",
        null = True,
        default=None
    )
    cpf = models.CharField(
        db_column = "usr_cpf",
        max_length = 11,
        unique = True
    )
    email = models.EmailField(
        max_length = 254,
        db_column = "usr_email",
        unique = True
    )
    password = models.CharField(
        db_column = "usr_password",
        max_length = 255
    )
    phone = models.CharField(
        db_column = "usr_phone",
        max_length = 50
    )
    is_superuser = models.BooleanField(
        db_column = "usr_is_superuser",
        default = False
    )
    is_active = models.BooleanField(
        db_column = "usr_is_active",
        default = True
    )
    created_at = models.DateTimeField(
        auto_now_add= True,
        db_column = "usr_created_at"
    )
    updated_at = models.DateTimeField(
        auto_now= True,
        db_column = "usr_updated_at"
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","cpf","password","phone"]
    objects = UtilsUser()