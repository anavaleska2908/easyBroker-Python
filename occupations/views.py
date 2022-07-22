from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from occupations.models import Occupation
from occupations.serializers import OccupationSerializer


class OccupationView(ListCreateAPIView):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer


class OccupationViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Occupation.objects.all()
    serializer_class = OccupationSerializer
