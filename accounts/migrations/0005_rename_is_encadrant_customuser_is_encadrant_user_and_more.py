# Generated by Django 4.1 on 2023-07-29 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_alter_customuser_options"),
    ]

    operations = [
        migrations.RenameField(
            model_name="customuser",
            old_name="is_encadrant",
            new_name="is_encadrant_user",
        ),
        migrations.RenameField(
            model_name="customuser", old_name="is_intern", new_name="is_intern_user",
        ),
    ]