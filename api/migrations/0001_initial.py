# Generated by Django 3.0.2 on 2020-02-29 16:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WellnessEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField()),
                ('date', models.DateField(default=datetime.date.today)),
                ('sleep_score', models.IntegerField()),
                ('energy_score', models.IntegerField()),
                ('soreness_score', models.IntegerField()),
                ('mood_score', models.IntegerField()),
                ('stress_score', models.IntegerField()),
                ('total_score', models.IntegerField()),
            ],
            options={
                'unique_together': {('user', 'date')},
            },
        ),
    ]