# Generated by Django 3.0.2 on 2020-03-05 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wellnessentry',
            name='comments',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
