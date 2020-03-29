from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class WellnessEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    sleep_score = models.IntegerField(null=False, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    energy_score = models.IntegerField(null=False, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    soreness_score = models.IntegerField(null=False, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    mood_score = models.IntegerField(null=False, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    stress_score = models.IntegerField(null=False, default=0, validators=[MaxValueValidator(5), MinValueValidator(0)])
    total_score = models.IntegerField(null=False, default=0, validators=[MaxValueValidator(25), MinValueValidator(0)])
    comments = models.CharField(max_length=200, null=True)

    class Meta:
        unique_together = ('user', 'date')

    # Figure out how to use
    # def __str__(self):
    #     return self.user.username + "-" + self.date
