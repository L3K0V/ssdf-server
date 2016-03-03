from rest_framework import serializers

from api.competitions.models import Competition
from api.events.models import Event

class CompetitionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        e = Event.objects.get(pk=self.context.get('event_pk'))
        return Competition.objects.create(event=e, **validated_data)

    class Meta:
        model = Competition
        fields = ('id', 'name', 'description', 'type')
