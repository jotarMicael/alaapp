# Generated by Django 4.1.1 on 2022-10-15 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ludoscienceapp", "0004_alter_proyect_image_alter_user_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_image",
            field=models.ImageField(
                default="ludoscienceapp/static/profile_image/user.png",
                upload_to="ludoscienceapp/static/profile_image/",
            ),
        ),
    ]