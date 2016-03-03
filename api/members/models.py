from django.db import models
from django.contrib.auth.models import User

from django_countries.fields import CountryField


class Member(models.Model):
    user = models.OneToOneField(User, related_name='member')
    country = CountryField()


class Person(models.Model):

    BEGINNER = 'B'
    INTERMEDIATE = 'I'
    INTERMIDIATE_ADVANCED = 'IA'
    ADVANCED = 'A'
    ADVANCED_PLUS = 'AP'

    PERSON_LEVEL = (
        (BEGINNER, 'Beginner'),
        (INTERMEDIATE, 'Intermediate'),
        (INTERMIDIATE_ADVANCED, 'Intermidiate-Advanced'),
        (ADVANCED, 'Advanced'),
        (ADVANCED_PLUS, 'Advanced Plus')
    )

    member = models.OneToOneField('Member', related_name='person')
    level = models.CharField(max_length=2, choices=PERSON_LEVEL, default=BEGINNER)
