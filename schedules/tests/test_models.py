from django.test import TestCase
from schedules.models import Schedule
from users.models import User
from companies.models import Company
from properties.models import Property


class ScheduleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(
            dba="Ciusvini Softerhouse LDTA.",
            corporate_name="Vinihouse Show Show.",
            municipal_registration="123654789",
            state_registration="321654789",
            email="vinicius@vinihouse.com",
            phone="41992232701",
            cnpj="12345698750250"
        )
        cls.client = User.objects.create(
            first_name="Ana Valeska",
            last_name="Santos",
            cpf="05621167538",
            phone="75991627123",
            birthdate="1993-02-13",
            email="avaleska2908@gmail.com",
            password="123456"
        )
        cls.broker = User.objects.create(
            first_name="Vinicius",
            last_name="Rocha",
            cpf="03254687921",
            phone="4199222331",
            birthdate="1998-10-23",
            email="vinicius.rocha1.pereira1@outlook.com",
            password="004456"
        )
        cls.properties_list = [
            Property.objects.create(
                property_registration="112354456",
                description="This house is white and ugly",
                status_situation=1,
                status_condominium=0,
                status_service=1,
                status_type=0,
                status_garage=3,
                qty_bedrooms=2,
                qty_suites=1,
                qty_garage_vacancies=2,
                qty_bathroom=2
            )
        ]
        cls.schedules = Schedule.objects.create(
            comments="Teste do agendamento post",
            status_schedule=0,
            start_time="2022-05-25 14:30:00",
            end_time="2022-05-25 16:30:00",
            client=cls.client,
            company=cls.company,
            broker=cls.broker
        )

    def test_id_unique_constrain(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        id_unique_constrain = schedule._meta.get_field("id").unique
        self.assertTrue(id_unique_constrain)

    def test_schedule_comments_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        comments_label = schedule._meta.get_field("comments").verbose_name
        self.assertEquals(comments_label, "comments")

    def test_schedule_status_schedule_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        status_schedule_label = schedule._meta.get_field(
            "status_schedule").verbose_name
        self.assertEquals(status_schedule_label, "status schedule")

    def test_schedule_start_time_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        start_time_label = schedule._meta.get_field(
            "start_time").verbose_name
        self.assertEquals(start_time_label, "start time")

    def test_schedule_end_time_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        end_time_label = schedule._meta.get_field(
            "end_time").verbose_name
        self.assertEquals(end_time_label, "end time")

    def test_schedule_client_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        client_label = schedule._meta.get_field(
            "client").verbose_name
        self.assertEquals(client_label, "client")

    def test_schedule_broker_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        broker_label = schedule._meta.get_field(
            "broker").verbose_name
        self.assertEquals(broker_label, "broker")

    def test_schedule_company_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        company_label = schedule._meta.get_field(
            "company").verbose_name
        self.assertEquals(company_label, "company")

    def test_created_at_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        created_at_label = schedule._meta.get_field("created_at").verbose_name
        self.assertEquals(created_at_label, "created at")

    def test_updated_at_label(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        updated_at_label = schedule._meta.get_field("updated_at").verbose_name
        self.assertEquals(updated_at_label, "updated at")

    def test_schedule_client_null(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        client_received = schedule._meta.get_field("client").null
        self.assertTrue(client_received)

    def test_schedule_broker_null(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        broker_received = schedule._meta.get_field("broker").null
        self.assertTrue(broker_received)

    def test_schedule_company_null(self):
        schedule = Schedule.objects.get(id=self.schedules.id)
        company_received = schedule._meta.get_field("company").null
        self.assertTrue(company_received)
