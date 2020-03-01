from django.db import models

class Songs(models.Model):
    title = models.CharField(max_length=255, null=False)
    artist = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)

class Restaurant(models.Model):
    name = models.CharField(max_length=255, null=False)
    latitude = models.CharField(max_length=255, null=False)
    longitude = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
