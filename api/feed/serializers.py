from rest_framework import serializers

from push_notifications.models import APNSDevice, GCMDevice

from api.feed.models import FeedItem


class FeedItemSerializer(serializers.ModelSerializer):

    def create(self, validated_attrs):
        devices = GCMDevice.objects.all()
        devices.send_message("There are new news about the festival")

        devices = APNSDevice.objects.all()
        devices.send_message("There are new news about the festival")
        return super(FeedItemSerializer, self).create(validated_attrs)

    class Meta:
        model = FeedItem
        fields = ('id', 'event', 'title', 'text', 'created_at', 'updated_at', 'cover')
