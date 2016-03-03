from rest_framework import serializers

from api.feed.models import FeedItem


class FeedItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeedItem
        fields = ('id', 'event', 'title', 'text', 'created_at', 'updated_at', 'cover')
