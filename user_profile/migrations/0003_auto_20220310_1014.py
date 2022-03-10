# Generated by Django 3.2 on 2022-03-10 10:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20220308_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(default=16, validators=[django.core.validators.MinValueValidator(16), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.IntegerField(choices=[(0, 'I Prefer Not To Say'), (1, 'Male'), (2, 'Female')], default=0),
        ),
    ]
