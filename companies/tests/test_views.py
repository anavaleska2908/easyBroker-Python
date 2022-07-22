from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class TestCompanyView(APITestCase):
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
        self.req_endpoint = "/api/companies/"
        self.req_body_post = {
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
            "address": {
                "uf": "PR",
                "city": "Curitiba",
                "neighborhood": "Centro",
                "street": "Orlindo de Carvalho",
                "complement": "Prédio",
                "number": "2545",
                "cep": "78958238"
            }
        }
        self.post_res = self.client.post(self.req_endpoint,self.req_body_post,format="json") or None
        self.req_body_patch = {"dba": "Valid field on update"}
        self.req_body_required = {"dba": "Missing all others required fields for post"}
        self.req_body_not_allowed = {"cnpj": "Not allowed field on update"}
        self.req_id = self.post_res.data["id"] or None

    def test_create_company(self):
        self.assertEqual(self.post_res.status_code, status.HTTP_201_CREATED)

    def test_list_company(self):
        response = self.client.get(self.req_endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_show_company(self):
        response = self.client.get(f'{self.req_endpoint}{self.req_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_company(self):
        response = self.client.patch(f'{self.req_endpoint}{self.req_id}/',self.req_body_patch, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_company(self):
        response = self.client.delete(f'{self.req_endpoint}{self.req_id}/')
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
            
    def test_required_fields_create_company(self):
        response = self.client.post(self.req_endpoint,self.req_body_required,format="json") or None
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_not_allowed_fields_update_company(self):
        response = self.client.patch(f'{self.req_endpoint}{self.req_id}/',self.req_body_not_allowed,format="json")
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
