from django.test import TestCase
from schedules.models import Schedule
from users.models import User
from companies.models import Company
from addresses.models import Address


class CompanyModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            first_name= "Jane",
            last_name= "Doe",
            cpf= "13578572811",
            email= "janedoeuser@test.com",
            phone= "4199187524",
            birthdate= "1998-10-23",
            password= "123456"
        )
        cls.andress = Address.objects.create(
            uf= "PR",
            city= "Curitiba",
            neighborhood= "Centro",
            street= "Orlindo de Carvalho",
            complement= "Prédio",
            number= "2545",
            cep= "78958238"
        )
        cls.model_create = Company.objects.create(
            dba = "InssCoders Softerhouse LDTA.",
            corporate_name = "InsCoder",
            municipal_registration = "123654789",
            state_registration = "321654789",
            email = "diretoria@insscoders.com",
            phone = "41992232701",
            cnpj = "33125455690411"
        )
        cls.model_get = Company.objects.get(id = cls.model_create.id)
        cls.unique_fields = ["id","cnpj"]
        cls.not_null_fields = [
            "dba",
            "corporate_name",
            "municipal_registration",
            "state_registration",
            "email",
            "phone",
            "cnpj",
            "created_at",
            "updated_at",
        ]
        cls.valid_fields = cls.not_null_fields

    def test_unique_constrains(self):
        is_unique = True
        for field in self.unique_fields:
            is_unique = self.model_get._meta.get_field(field).unique
            if not is_unique: break
            
        self.assertTrue(is_unique)
        
    def test_not_null_constrains(self):
        is_null = False
        for field in self.not_null_fields:
            is_null = self.model_get._meta.get_field(field).null
            if is_null: break
            
        self.assertFalse(is_null)

    def test_valid_fields(self):
        for field in self.not_null_fields:
            result = self.model_get._meta.get_field(field).verbose_name
            self.assertEquals(result, field.replace('_', ' '))