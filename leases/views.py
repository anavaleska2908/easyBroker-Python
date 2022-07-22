from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from leases.models import Lease
from properties.models import Property
from leases.serializers import LeaseSerializer


class LeaseView(ListCreateAPIView,):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    
class LeaseViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer
    
class LeasePropertyViewDetails(ListAPIView):
    queryset = Lease.objects.all()
    serializer_class = LeaseSerializer

    def get_queryset(self):
        self.property = get_object_or_404(Property, pk=self.kwargs['pk'])
        return Lease.objects.filter(property=self.property)
        