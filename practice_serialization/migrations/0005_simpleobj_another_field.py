# Generated by Django 3.0.2 on 2020-03-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice_serialization', '0004_simpleobj'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleobj',
            name='another_field',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
