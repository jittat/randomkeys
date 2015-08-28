from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.title


class Keyword(models.Model):
    name = models.CharField(max_length=100)
    room = models.ForeignKey('Room')

    def __unicode__(self):
        return self.name
