from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from schedules.models import Schedule
from schedules.serializers import ScheduleSerializer


class ScheduleView(ListCreateAPIView,):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    
class ScheduleViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer