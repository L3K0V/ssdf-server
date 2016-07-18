from rest_framework import serializers

from push_notifications.models import APNSDevice, GCMDevice

from api.feed.models import FeedItem


class FeedItemSerializer(serializers.ModelSerializer):

    def create(self, validated_attrs):

        devices = GCMDevice.objects.all()
        devices.send_message("{}: {}...".format(validated_attrs.get('title')[:64], validated_attrs.get('text')[:64]))

        devices = APNSDevice.objects.all()
        devices.send_message("{}: {}...".format(validated_attrs.get('title')[:64], validated_attrs.get('text')[:64]))
        return super(FeedItemSerializer, self).create(validated_attrs)

    class Meta:
        model = FeedItem
        fields = ('id', 'event', 'title', 'text', 'created_at', 'updated_at', 'cover')
