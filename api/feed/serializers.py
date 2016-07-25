from rest_framework import serializers

from push_notifications.models import APNSDevice, GCMDevice

from api.feed.models import FeedItem


class FeedItemSerializer(serializers.ModelSerializer):

    def create(self, validated_attrs):

        item = super(FeedItemSerializer, self).create(validated_attrs)

        devices = APNSDevice.objects.all()
        devices.send_message("{}: {}...".format(item.title[:64], item.text[:64]), extra={"feeditem": item.id})

        devices = GCMDevice.objects.all()
        devices.send_message("{}: {}...".format(item.title[:64], item.text[:64]), extra={"feeditem": item.id})

        return item

    class Meta:
        model = FeedItem
        fields = ('id', 'event', 'title', 'text', 'created_at', 'updated_at', 'cover')
