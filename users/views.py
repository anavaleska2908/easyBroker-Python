from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response, status
from users.models import User
from users.permissions import UserPermission
from users.serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate


class UserView(ListCreateAPIView,):
    permission_classes = [UserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = []
    
    def post(self,req):
        try: 
            user = self._authenticate(req.data)
            token = self._generate_token(user)
            return Response({"token": token}, status.HTTP_200_OK)
        except:
            return Response({"detail": ["invalid email or password."]}, status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def _authenticate(login):
        email, password , *_ = login.values()
        user = authenticate(
            username = email,
            password = password
        )
        return user
    
    @staticmethod
    def _generate_token(user):
        token = RefreshToken.for_user(user)
        return str(token.access_token)