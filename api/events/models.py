from django.db import models
from django.contrib.gis.db import models as gis_model

from django_countries.fields import CountryField


class Event(models.Model):
    name = models.CharField(max_length=64, blank=False, null=False)
    description = models.TextField()

    country = CountryField()
    city = models.CharField(max_length=32, blank=True, null=False)

    people = models.ManyToManyField('members.Person', through='EventPerson', through_fields=('event', 'person'), related_name='events')

    from_date = models.DateTimeField()
    to_date = models.DateTimeField()

    def __str__(self):
        return '{}'.format(self.name)


class EventTrack(models.Model):

    COUPLES = 'C'
    INDIVIDUALS = 'I'

    TRACK_TYPE = (
        (COUPLES, 'Couples'),
        (INDIVIDUALS, 'Individuals')
    )

    name = models.CharField(max_length=64, blank=False, null=False, unique=True)
    type = models.CharField(max_length=1, choices=TRACK_TYPE, default=COUPLES)
    event = models.ForeignKey('Event', related_name='tracks')

    def __str__(self):
        return '{} ({})'.format(self.name, self.type)


class EventTrackLevel(models.Model):

    BEGINNER = 'B'
    INTERMEDIATE = 'I'
    INTERMIDIATE_ADVANCED = 'IA'
    ADVANCED = 'A'
    ADVANCED_PLUS = 'AP'

    TRACK_LEVEL = (
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (INTERMIDIATE_ADVANCED, 'Intermidiate-Advanced'),
        (ADVANCED, 'Advanced'),
        (ADVANCED_PLUS, 'Advanced Plus')
    )

    capacity = models.PositiveSmallIntegerField(blank=False)
    track = models.ForeignKey('EventTrack', related_name='levels')
    level = models.CharField(max_length=2, choices=TRACK_LEVEL, default=BEGINNER)

    class Meta:
        unique_together = ('track', 'level')


class EventPerson(models.Model):

    TEACHER = 'T'
    STUDENT = 'S'
    DJ = 'D'
    GUEST = 'G'

    PERSON_TYPE = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (DJ, 'DJ'),
        (GUEST, 'Guest')
    )

    event = models.ForeignKey('Event', related_name='person')
    person = models.ForeignKey('members.Person', related_name='event')
    type = models.CharField(max_length=1, choices=PERSON_TYPE, default=STUDENT)

    class Meta:
        unique_together = ('event', 'person')


class ScheduleItem(gis_model.Model):

    PARTY = 'P'
    MAIN_CLASS = 'M'
    TASTER_CLASS = 'T'
    OTHER_ACTIVITY = 'A'

    SCHEDULE_TYPE = (
        (PARTY, 'Party'),
        (MAIN_CLASS, 'Main class'),
        (TASTER_CLASS, 'Taster class'),
        (OTHER_ACTIVITY, 'Other activity')
    )

    event_track_level = models.ForeignKey('EventTrackLevel', related_name='schedule')
    type = models.CharField(max_length=1, choices=SCHEDULE_TYPE, default=PARTY)

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    point = gis_model.PointField()


class OpeningHours(gis_model.Model):
    description = models.TextField()
    schedule_item = models.ForeignKey('ScheduleItem', related_name='hours')
    from_datetime = models.DateTimeField()
    to_datetime = models.DateTimeField()
