from django.urls import path
from users.views import UserView, UserViewDetails


urlpatterns = [
    path('', UserView.as_view()),
    path('<str:pk>/', UserViewDetails.as_view())
]