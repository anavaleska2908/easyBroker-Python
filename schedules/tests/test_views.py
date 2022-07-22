from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class TestScheduleView(APITestCase):
    def setUp(self):
        self.user_obj = User.objects.create(
            first_name="Jane",
            last_name="Doe",
            cpf="13578571811",
            email="janedoeuserdata@test.com",
            phone="4199187524",
            birthdate="1998-10-23",
            password="123456"
        )
        self.client.force_authenticate(user=self.user_obj)
        self.client_data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "cpf": "12345678910",
            "phone": "55912345678",
            "birthdate": "1993-02-13",
            "email": "janedoe@test.com",
            "password": "123456"
        }
        self.address_data = {
            "uf": "PR",
            "city": "Curitiba",
            "neighborhood": "Centro",
            "street": "Orlindo de Carvalho",
            "complement": "Prédio",
            "number": "2545",
            "cep": "78958238"
        }
        self.company_data = {
            "dba": "InssCoders Softerhouse LDTA.",
            "corporate_name": "InsCoder",
            "municipal_registration": "123654789",
            "state_registration": "321654789",
            "email": "diretoria@insscoders.com",
            "phone": "41992232701",
            "cnpj": "33125455690411",
            "user": {
                "first_name": "Jane",
                "last_name": "Doe",
                "cpf": "13578572811",
                "email": "janedoeuser@test.com",
                "phone": "4199187524",
                "birthdate": "1998-10-23",
                "password": "123456"
            },
            "address": self.address_data
        }
        self.broker_data = {
            "first_name": "John",
            "last_name": "Doe",
            "cpf": "12345678911",
            "phone": "4199121311",
            "birthdate": "1998-10-23",
            "email": "johndoe@test.com",
            "password": "123456"
        }
        self.company_id = self.client.post("/api/companies/",self.company_data,format="json").json()["id"]
        self.client_id = self.client.post("/api/users/",self.client_data,format="json").json()["id"]
        self.broker_id = self.client.post("/api/users/",self.broker_data,format="json").json()["id"]
        self.property_data = {
            "property_registration": "112354456",
            "description": "This house is white and ugly",
            "status_situation": 1,
            "status_condominium": 0,
            "status_service": 1,
            "status_type": 0,
            "status_garage": 3,
            "qty_bedrooms": 2,
            "qty_suites": 1,
            "qty_garage_vacancies": 2,
            "qty_bathroom": 2,
            "property_value": 1500,
            "user": self.broker_id,
            "address": self.address_data
        }
        self.property_id = self.client.post("/api/properties/",self.property_data,format="json").json()["id"]
        self.schedules_data = {
            "comments": "Schedule Test",
            "status_schedule": 0,
            "start_time": "2022-05-25 14:30:00",
            "end_time": "2022-05-25 16:30:00",
            "company": self.company_id,
            "client": self.client_id,
            "broker": self.broker_id,
            "properties_list": [self.property_id]
        }
        self.schedules = self.client.post("/api/schedules/",self.schedules_data,format="json") or None

    def test_only_authenticated_user_can_create_a_schedule(self):
        self.assertEqual(self.schedules.status_code, status.HTTP_201_CREATED)

    def test_only_authenticated_user_can_list_all_schedule(self):
        response = self.client.get("/api/schedules/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_authenticated_user_can_get_one_schedule(self):
        response = self.client.get(f'/api/schedules/{self.schedules.data["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_only_authenticated_user_can_update_a_schedule(self):
        response = self.client.patch(f'/api/schedules/{self.schedules.data["id"]}/',{
            "comments": "Schedule Test updated."
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_forbidden_fields_update_a_schedule(self):
        response = self.client.patch(f'/api/schedules/{self.schedules.data["id"]}/',{
            "client": "",
            "broker": "",
            "company": "",
            "properties_list": [""]
        },format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_only_authenticated_user_can_delete_a_schedule(self):
        response = self.client.delete(f'/api/schedules/{self.schedules.data["id"]}/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
