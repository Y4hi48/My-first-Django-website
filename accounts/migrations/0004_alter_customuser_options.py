# Generated by Django 4.1 on 2023-07-28 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_customuser_options_customuser_is_encadrant_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser", options={"verbose_name_plural": "Custom users"},
        ),
    ]
