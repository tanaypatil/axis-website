from django.db import models
from django.core.validators import RegexValidator


class AmishRegistrations(models.Model):
    idnum = models.CharField(null=True, default=None, max_length=20)
    name = models.CharField(max_length=40, blank=False)
    college = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=25, blank=False)
    contact = models.CharField(max_length=12, blank=False, null=False, default=None, unique=True,
                               validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid phone number.')])
    mail = models.EmailField(blank=False, unique=True, null=False, default=None)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class FeedBackFromAndroid(models.Model):
    name = models.CharField(max_length=40)
    contact = models.CharField(max_length=13)
    mail = models.EmailField()
    msg = models.TextField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class NotifsAndroid(models.Model):
    title = models.CharField(max_length=50)
    msg = models.TextField(max_length=200)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
