# Generated by Django 3.0.2 on 2020-03-13 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('practice_serialization', '0005_simpleobj_another_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='simpleobj',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='practice_serialization.Comment'),
        ),
    ]
