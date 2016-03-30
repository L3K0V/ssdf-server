from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from api.events.models import Event
from api.guide.models import GuideItem, OpeningHours


class GuideItemSerializer(GeoFeatureModelSerializer):

    def create(self, validated_data):
        e = Event.objects.get(pk=self.context.get('event_pk'))
        return GuideItem.objects.create(event=e, **validated_data)

    class Meta:
        depth = 1
        model = GuideItem
        geo_field = 'point'
        auto_bbox = True
        id_field = False
        fields = ('id', 'name', 'description', 'address', 'city', 'state', 'hours')


class GuideItemHoursSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        g = GuideItem.objects.get(pk=self.context.get('guide_pk'))
        return OpeningHours.objects.create(guide_item=g, **validated_data)

    class Meta:
        model = OpeningHours
        fields = ('id', 'description', 'from_datetime', 'to_datetime')
