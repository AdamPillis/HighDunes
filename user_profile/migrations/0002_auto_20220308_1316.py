# Generated by Django 3.2 on 2022-03-08 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='f_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='l_name',
            new_name='last_name',
        ),
    ]
