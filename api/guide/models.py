from django.contrib.gis.db import models


class GuideItem(models.Model):
    event = models.ForeignKey('events.Event', related_name='items')
    name = models.CharField(max_length=48)
    description = models.TextField()

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    point = models.PointField()


class OpeningHours(models.Model):
    guide_item = models.ForeignKey('GuideItem', related_name='hours')

    description = models.TextField()

    from_datetime = models.DateTimeField()
    to_datetime = models.DateTimeField()
