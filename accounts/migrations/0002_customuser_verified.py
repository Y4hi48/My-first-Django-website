# Generated by Django 4.1 on 2023-07-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="verified",
            field=models.BooleanField(default=False),
        ),
    ]
