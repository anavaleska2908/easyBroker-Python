from django.urls import path
from companies.views import CompanyView, CompanyViewDetails


urlpatterns = [
    path('', CompanyView.as_view()),
    path('<str:pk>/', CompanyViewDetails.as_view())
]