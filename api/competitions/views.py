from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import response
from rest_framework import status

from api.competitions.models import Competition
from api.competitions.serializers import CompetitionSerializer


class CompetitionViewSet(viewsets.ModelViewSet):
    queryset = Competition.objects.all()
    serializer_class = CompetitionSerializer

    def create(self, request, event_pk=None):
        context = {'request': request, 'event_pk': event_pk}
        serializer = CompetitionSerializer(context=context, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, event_pk=None):
        queryset = Competition.objects.filter(event=event_pk)
        serializer = CompetitionSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None):
        queryset = Competition.objects.filter(pk=pk, event=event_pk)
        track = get_object_or_404(queryset, pk=pk)
        serializer = CompetitionSerializer(track, context={'request': request})
        return response.Response(serializer.data)
