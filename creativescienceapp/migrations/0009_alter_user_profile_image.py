# Generated by Django 4.1.1 on 2022-10-01 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("creativescienceapp", "0008_rename_image_profile_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                blank=True, null=True, upload_to="creativescience/static/profile_image"
            ),
        ),
    ]
