from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from properties.models import Property
from properties.permissions import PropertyPermission
from properties.serializers import PropertySerializer


class PropertyView(ListCreateAPIView,):
    permission_classes = [PropertyPermission]
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    
class PropertyViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer