from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from addresses.models import Address
from addresses.serializers import AddressSerializer


class AddressView(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    
class AddressViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer