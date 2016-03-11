from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import response
from rest_framework import status

from api.guide.models import GuideItem, OpeningHours
from api.guide.serializers import GuideItemSerializer, GuideItemHoursSerializer


class GuideItemViewSet(viewsets.ModelViewSet):
    queryset = GuideItem.objects.all()
    serializer_class = GuideItemSerializer

    def create(self, request, event_pk=None):
        context = {'request': request, 'event_pk': event_pk}
        serializer = GuideItemSerializer(context=context, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, event_pk=None):
        queryset = GuideItem.objects.filter(event=event_pk)
        serializer = GuideItemSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None):
        queryset = GuideItem.objects.filter(pk=pk, event=event_pk)
        track = get_object_or_404(queryset, pk=pk)
        serializer = GuideItemSerializer(track, context={'request': request})
        return response.Response(serializer.data)


class GuideItemHoursViewSet(viewsets.ModelViewSet):
    queryset = OpeningHours.objects.all()
    serializer_class = GuideItemHoursSerializer

    def create(self, request, event_pk=None, guide_pk=None):
        context = {'request': request, 'event_pk': event_pk, 'guide_pk': guide_pk}
        serializer = GuideItemHoursSerializer(context=context, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, event_pk=None, guide_pk=None):
        queryset = OpeningHours.objects.filter(guide_item=guide_pk)
        serializer = GuideItemHoursSerializer(queryset, many=True, context={'request': request})
        return response.Response(serializer.data)

    def retrieve(self, request, pk=None, event_pk=None, guide_pk=None):
        queryset = OpeningHours.objects.filter(pk=pk, guide_item=guide_pk)
        track = get_object_or_404(queryset, pk=pk)
        serializer = GuideItemHoursSerializer(track, context={'request': request})
        return response.Response(serializer.data)
