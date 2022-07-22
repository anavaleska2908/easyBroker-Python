from django.urls import path
from schedules.views import ScheduleView, ScheduleViewDetails


urlpatterns = [
    path('', ScheduleView.as_view()),
    path('<str:pk>/', ScheduleViewDetails.as_view())
]