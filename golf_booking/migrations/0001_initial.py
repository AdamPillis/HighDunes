# Generated by Django 3.2 on 2022-03-10 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('number_of_holes', models.IntegerField(choices=[(9, '9'), (18, '18')], default=0)),
                ('number_of_players', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0)),
                ('club_hire', models.BooleanField(default=False)),
                ('play_date', models.DateField()),
                ('play_time', models.IntegerField(choices=[(8, '8:00'), (9, '9:00'), (10, '10:00'), (11, '11:00'), (12, '12:00'), (1, '13:00'), (2, '14:00'), (3, '15:00'), (4, '16:00'), (5, '17:00')], default=False)),
                ('extra_requests', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]