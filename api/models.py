from django.db import models
from datetime import date
# Create your models here.

class WellnessEntry(models.Model):
    user = models.IntegerField()
    date = models.DateField(default=date.today)
    sleep_score = models.IntegerField()
    energy_score = models.IntegerField()
    soreness_score = models.IntegerField()
    mood_score = models.IntegerField()
    stress_score = models.IntegerField()
    total_score = models.IntegerField()

    class Meta:
        unique_together = ('user', 'date')
