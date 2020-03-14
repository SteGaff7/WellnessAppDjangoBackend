from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from datetime import datetime


class Comment(models.Model):

    content = models.CharField(max_length=200)
    created = models.DateTimeField(default=now)


class SimpleObj(models.Model):

    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True)
    my_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=100)
    another_field = models.CharField(max_length=100, null=True)


class ObjCreatedByUser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created = models.DateTimeField(default=now)
