from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import response
from rest_framework import status

from api.feedback.models import EventTrackLevelRate, ScheduleItemRate
from api.feedback.serializers import EventTrackLevelRateSerializer, ScheduleItemRateSerializer


class EventTrackLevelRateViewSet(viewsets.ModelViewSet):
    queryset = EventTrackLevelRate.objects.all()
    serializer_class = EventTrackLevelRateSerializer

    def create(self, request, event_pk=None, track_pk=None, level_pk=None):
        context = {'request': request, 'event_pk': event_pk, 'track_pk': track_pk, 'level_pk': level_pk}
        serializer = EventTrackLevelRateSerializer(context=context, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, event_pk=None, track_pk=None, level_pk=None):
        queryset = EventTrackLevelRate.objects.filter(event_track_level=level_pk)
        serializer = EventTrackLevelRateSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None, track_pk=None, level_pk=None):
        queryset = EventTrackLevelRate.objects.filter(pk=pk, event_track_level=level_pk)
        level = get_object_or_404(queryset, pk=pk)
        serializer = EventTrackLevelRateSerializer(level, context={'request': request})
        return response.Response(serializer.data)


class ScheduleItemRateViewSet(viewsets.ModelViewSet):
    queryset = ScheduleItemRate.objects.all()
    serializer_class = ScheduleItemRateSerializer

    def create(self, request, event_pk=None, track_pk=None, level_pk=None, schedule_pk=None):
        context = {'request': request, 'event_pk': event_pk, 'track_pk': track_pk, 'level_pk': level_pk, 'schedule_pk': schedule_pk}
        serializer = ScheduleItemRateSerializer(context=context, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, event_pk=None, track_pk=None, level_pk=None, schedule_pk=None):
        queryset = ScheduleItemRate.objects.filter(schedule_item=schedule_pk)
        serializer = ScheduleItemRateSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None, track_pk=None, level_pk=None, schedule_pk=None):
        queryset = ScheduleItemRate.objects.filter(pk=pk, schedule_item=schedule_pk)
        level = get_object_or_404(queryset, pk=pk)
        serializer = ScheduleItemRateSerializer(level, context={'request': request})
        return response.Response(serializer.data)
