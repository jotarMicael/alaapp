# Generated by Django 4.1.1 on 2022-11-09 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ludoscienceapp', '0004_remove_challenge_checkin_badge_area_badge_checkin_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='checkin',
            field=models.ManyToManyField(related_name='challenge_checkins', to='ludoscienceapp.checkin'),
        ),
        migrations.AlterField(
            model_name='badge',
            name='checkin',
            field=models.ManyToManyField(related_name='badge_checkins', to='ludoscienceapp.checkin'),
        ),
    ]