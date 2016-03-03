from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class EventTrackLevelRate(models.Model):
    event_track_level = models.ForeignKey('events.EventTrackLevel')
    email = models.EmailField()

    feedback = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    comment = models.TextField(max_length=8*1024)

    unique_together = ('event_track_level', 'email')


class ScheduleItemRate(models.Model):
    schedule_item = models.ForeignKey('events.ScheduleItem')
    email = models.EmailField()

    feedback = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    comment = models.TextField(max_length=8*1024)

    unique_together = ('schеdule_item', 'email')
