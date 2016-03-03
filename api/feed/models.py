from django.db import models


class FeedItem(models.Model):
    event = models.ForeignKey('events.Event', related_name='feed')

    title = models.CharField(max_length=64)
    text = models.TextField(max_length=8096)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    cover = models.FileField(blank=True, null=True)

    urls = models.ManyToManyField('FeedItemUrl')


class FeedItemUrl(models.Model):
    url = models.URLField()
