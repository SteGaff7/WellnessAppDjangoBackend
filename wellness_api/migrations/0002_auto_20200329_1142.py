# Generated by Django 3.0.2 on 2020-03-29 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wellness_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wellnessentry',
            name='energy_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wellnessentry',
            name='mood_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wellnessentry',
            name='sleep_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wellnessentry',
            name='soreness_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wellnessentry',
            name='stress_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wellnessentry',
            name='total_score',
            field=models.IntegerField(default=0),
        ),
    ]
