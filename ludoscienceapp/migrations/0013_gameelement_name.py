# Generated by Django 4.1.1 on 2022-10-25 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ludoscienceapp", "0012_area_alter_gameelement_area"),
    ]

    operations = [
        migrations.AddField(
            model_name="gameelement",
            name="name",
            field=models.CharField(default="Algo", max_length=150, null=True),
        ),
    ]