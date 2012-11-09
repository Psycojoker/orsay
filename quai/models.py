from django.db import models


class Contact(models.Model):
    is_called = models.CharField(max_length=255)
    in_recontacting_loop = models.BooleanField(default=True)
    notes = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.is_called


class Meet(models.Model):
    place = models.CharField(max_length=255)
    contact = models.ForeignKey(Contact)
    description = models.TextField(null=True, blank=True)
    datetime = models.DateTimeField()
