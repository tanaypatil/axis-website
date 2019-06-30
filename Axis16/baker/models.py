from django.db import models


class Baker_Questions(models.Model):

    name = models.CharField(max_length=10, default="zero")
    img = models.FileField(upload_to='bkimg/')
    answer = models.CharField(max_length=100)
    hint = models.CharField(max_length=300)
    level = models.IntegerField()

    class Meta:
        ordering = ['level']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name
