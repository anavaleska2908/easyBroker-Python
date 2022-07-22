from django.urls import path
from properties.views import PropertyView, PropertyViewDetails


urlpatterns = [
    path('', PropertyView.as_view()),
    path('<str:pk>/', PropertyViewDetails.as_view())
]