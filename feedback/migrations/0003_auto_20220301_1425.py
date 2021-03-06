# Generated by Django 3.2 on 2022-03-01 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_alter_review_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
