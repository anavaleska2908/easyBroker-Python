from django.urls import path
from addresses.views import AddressView, AddressViewDetails


urlpatterns = [
    path('', AddressView.as_view()),
    path('<str:pk>/', AddressViewDetails.as_view())
]