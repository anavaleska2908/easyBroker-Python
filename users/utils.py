from django.contrib.auth.models import BaseUserManager


class UtilsUser(BaseUserManager):
    def create(self,**params):
        params["email"] = self.normalize_email(params["email"])
        new_user = self.model(**params)
        new_user.set_password(params["password"])
        new_user.save()
        return new_user         

    def create_superuser(self,**params):
        return self.create(is_superuser=True, **params)