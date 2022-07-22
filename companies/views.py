from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from companies.models import Company
from companies.permissions import CompanyPermission
from companies.serializers import CompanySerializer


class CompanyView(ListCreateAPIView,):
    permission_classes = [CompanyPermission]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
class CompanyViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer