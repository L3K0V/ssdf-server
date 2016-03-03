from rest_framework_gis.serializers import GeoFeatureModelSerializer

from api.events.models import Event
from api.guide.models import GuideItem


class GuideItemSerializer(GeoFeatureModelSerializer):
    def create(self, validated_data):
        e = Event.objects.get(pk=self.context.get('event_pk'))
        return GuideItem.objects.create(event=e, **validated_data)

    class Meta:
        depth = 1
        model = GuideItem
        geo_field = 'point'
        id_field = False
        fields = ('id', 'name', 'description', 'address', 'city', 'state', 'hours')
