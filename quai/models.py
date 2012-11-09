from django.db import models


class Person(models.Model):
    is_called = models.CharField(max_length=255)
    in_recontacting_loop = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.is_called


class Meet(models.Model):
    place = models.CharField(max_length=255)
    contact = models.ForeignKey(Person)
    description = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField()


class Mail(models.Model):
    email = models.EmailField()
    person = models.ForeignKey(Person)

    def __unicode__(self):
        return self.email
