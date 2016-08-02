from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from api.events.models import Event, EventPerson, EventTrack, EventTrackLevel, ScheduleItem, OpeningHours


class EventSerializer(serializers.ModelSerializer):

    url = serializers.HyperlinkedIdentityField(view_name='events-detail')

    class Meta:
        depth = 1
        model = Event
        fields = ('url', 'id', 'name', 'description', 'country', 'city', 'from_date', 'to_date', 'tracks')


class EventPersonSerializer(serializers.ModelSerializer):

    type = serializers.ChoiceField(
        choices=EventPerson.PERSON_TYPE,
        style={'base_template': 'radio.html', 'inline': 'true'}
    )

    class Meta:
        model = EventPerson
        fields = ('id', 'person', 'event', 'type')


class EventTrackSerializer(serializers.ModelSerializer):
        def create(self, validated_data):
            e = Event.objects.get(pk=self.context.get('event_pk'))
            return EventTrack.objects.create(event=e, **validated_data)

        class Meta:
            depth = 1
            model = EventTrack
            fields = ('id', 'name', 'type', 'levels')


class EventTrackLevelSerializer(serializers.ModelSerializer):
        def create(self, validated_data):
            t = EventTrack.objects.get(pk=self.context.get('track_pk'))
            return EventTrackLevel.objects.create(track=t, **validated_data)

        class Meta:
            depth = 1
            model = EventTrackLevel
            fields = ('id', 'capacity', 'level', 'schedule')


class ScheduleItemSerializer(GeoFeatureModelSerializer):
    def create(self, validated_data):
        l = EventTrackLevel.objects.get(pk=self.context.get('level_pk'))
        return ScheduleItem.objects.create(event_track_level=l, **validated_data)

    class Meta:
        depth = 1
        model = ScheduleItem
        geo_field = 'point'
        id_field = False
        fields = ('id', 'type', 'address', 'city', 'state', 'hours')


class ScheduleItemHoursSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        s = ScheduleItem.objects.get(pk=self.context.get('schedule_pk'))
        return OpeningHours.objects.create(schedule_item=s, **validated_data)

    class Meta:
        model = OpeningHours
        fields = ('id', 'description', 'from_datetime', 'to_datetime')
