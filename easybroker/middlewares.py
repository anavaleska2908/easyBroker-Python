from re import M
from rest_framework.views import Response, status
from rest_framework.renderers import JSONRenderer
import json


class customMiddleware():
    errors = []
    
    def __init__(self,get_response):
        self.get_response = get_response

    def __setup__(self,req):
        self.body = json.loads(req.body) if req.body else None
        self.endpoint = req.path.split('/')[2] or None
        self.method = req.method or None
    
    def __next__(self, req):
        return self.get_response(req)
    
    def __response__(self, content = {}, status = status.HTTP_200_OK):
        response = Response(content, status)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        self.errors = []
        return response

    def __call__(self, req):
        self.__setup__(req)
        self.validate_fields()
        return self.__response__(self.errors, status.HTTP_400_BAD_REQUEST) if bool(self.errors) else self.__next__(req)

    fields_mapping = {
        "login": {
            "POST": ["email","password"]
        },
        "users": {
            "POST": ["first_name","last_name","cpf","email","birthdate","password"],
            "PATCH": ["occupations","company","address"]
        },
        "companies": {
            "POST": [
                "dba",
                "corporate_name",
                "municipal_registration",
                "state_registration",
                "email",
                "phone",
                "cnpj",
                "address",
                "user"
            ],
            "PATCH": ["cnpj","address","user"]
        },
        "leases": {
            "POST": ["company","property","property_value"],
            "PATCH": ["company","property"]
        },
        "occupations": {
            "POST": ["name","company"],
            "PATCH": ["company"]
        },
        "properties": {
            "POST": [
                "property_registration",
                "description",
                "status_situation",
                "status_condominium",
                "status_service",
                "status_type",
                "status_garage",
                "qty_bedrooms",
                "qty_suites",
                "qty_garage_vacancies",
                "qty_bathroom",
                "property_value",
                "user",
                "address"
            ],
            "PATCH": ["property_registration","user","company","address"]
        },
        "schedules": {
            "POST": ["status_schedule","start_time","end_time","client","broker","properties_list"],
            "PATCH": ["client","company","broker","properties_list"]
        },
    }

    def validate_fields(self):
        errors_list = {}

        if ((self.endpoint in self.fields_mapping) and (self.method in self.fields_mapping[self.endpoint])):
            for field in self.fields_mapping[self.endpoint][self.method]:
                if (self.method == "POST" and not field in self.body):
                    errors_list[field] = ["This field is required."]

                elif (self.method == "PATCH" and field in self.body):
                    errors_list[field] = ["This field is not allowed."]

        if bool(errors_list): self.errors = errors_list
        