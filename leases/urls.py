from django.urls import path
from leases.views import LeasePropertyViewDetails, LeaseView, LeaseViewDetails


urlpatterns = [
    path('', LeaseView.as_view()),
    path('<str:pk>/', LeaseViewDetails.as_view()),
    path('property/<str:pk>/', LeasePropertyViewDetails.as_view())
]