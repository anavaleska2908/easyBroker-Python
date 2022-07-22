from django.urls import path
from occupations.views import OccupationView, OccupationViewDetails


urlpatterns = [
    path('', OccupationView.as_view()),
    path('<str:pk>/', OccupationViewDetails.as_view())
]
