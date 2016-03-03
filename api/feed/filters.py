import django_filters

from api.feed.models import FeedItem


class FeedItemFilter(django_filters.FilterSet):
    created = django_filters.DateTimeFilter(name='created_at', lookup_type='gte')
    updated = django_filters.DateTimeFilter(name='updated_at', lookup_type='gte')

    class Meta:
        model = FeedItem
        fields = ['event', 'created', 'updated']
