from rest_framework import serializers

from api.events.models import EventTrackLevel, ScheduleItem
from api.feedback.models import EventTrackLevelRate, ScheduleItemRate


class EventTrackLevelRateSerializer(serializers.ModelSerializer):
        def create(self, validated_data):
            e = EventTrackLevel.objects.get(pk=self.context.get('level_pk'))
            return EventTrackLevelRate.objects.create(event_track_level=e, **validated_data)

        class Meta:
            depth = 1
            model = EventTrackLevelRate
            fields = ('id', 'email', 'feedback', 'comment')


class ScheduleItemRateSerializer(serializers.ModelSerializer):
        def create(self, validated_data):
            e = ScheduleItem.objects.get(pk=self.context.get('schedule_pk'))
            return ScheduleItemRate.objects.create(schedule_item=e, **validated_data)

        class Meta:
            depth = 1
            model = ScheduleItemRate
            fields = ('id', 'email', 'feedback', 'comment')
