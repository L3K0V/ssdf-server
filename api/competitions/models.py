from django.db import models


class Competition(models.Model):

    COUPLES = 'C'
    INDIVIDUALS = 'I'

    TRACK_TYPE = (
        (COUPLES, 'Couples'),
        (INDIVIDUALS, 'Individuals')
    )

    event = models.ForeignKey('events.Event', related_name='competitions')
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=1, choices=TRACK_TYPE, default=COUPLES)
    description = models.TextField()
