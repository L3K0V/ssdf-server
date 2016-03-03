from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import response
from rest_framework import status

from api.events.models import Event, EventPerson, EventTrack, EventTrackLevel, ScheduleItem
from api.events.serializers import EventSerializer, EventPersonSerializer
from api.events.serializers import EventTrackSerializer, EventTrackLevelSerializer, ScheduleItemSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventPersonViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = EventPerson.objects.all()
    serializer_class = EventPersonSerializer


class EventTrackViewSet(viewsets.ModelViewSet):
    queryset = EventTrack.objects.all()
    serializer_class = EventTrackSerializer

    def create(self, request, event_pk=None):
        context = {'request': request, 'event_pk': event_pk}
        serializer = EventTrackSerializer(context=context, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, event_pk=None):
        queryset = EventTrack.objects.filter(event=event_pk)
        serializer = EventTrackSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None):
        queryset = EventTrack.objects.filter(pk=pk, event=event_pk)
        track = get_object_or_404(queryset, pk=pk)
        serializer = EventTrackSerializer(track, context={'request': request})
        return response.Response(serializer.data)


class EventTrackLevelViewSet(viewsets.ModelViewSet):
    queryset = EventTrackLevel.objects.all()
    serializer_class = EventTrackLevelSerializer

    def create(self, request, event_pk=None, track_pk=None):
        context = {'request': request, 'event_pk': event_pk, 'track_pk': track_pk}
        serializer = EventTrackLevelSerializer(context=context, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, event_pk=None, track_pk=None):
        queryset = EventTrackLevel.objects.filter(track__event=event_pk, track=track_pk)
        serializer = EventTrackLevelSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None, track_pk=None):
        queryset = EventTrackLevel.objects.filter(pk=pk, track__event=event_pk, track=track_pk)
        level = get_object_or_404(queryset, pk=pk)
        serializer = EventTrackLevelSerializer(level, context={'request': request})
        return response.Response(serializer.data)


class ScheduleItemViewSet(viewsets.ModelViewSet):
    queryset = ScheduleItem.objects.all()
    serializer_class = ScheduleItemSerializer

    def create(self, request, event_pk=None, track_pk=None, level_pk=None):
        context = {'request': request, 'event_pk': event_pk, 'track_pk': track_pk, 'level_pk': level_pk}
        serializer = ScheduleItemSerializer(context=context, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, event_pk=None, track_pk=None, level_pk=None):
        queryset = ScheduleItem.objects.filter(event_track_level=level_pk)
        serializer = ScheduleItemSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None, track_pk=None, level_pk=None):
        queryset = ScheduleItem.objects.filter(pk=pk, event_track_level=level_pk)
        level = get_object_or_404(queryset, pk=pk)
        serializer = ScheduleItemSerializer(level, context={'request': request})
        return response.Response(serializer.data)
