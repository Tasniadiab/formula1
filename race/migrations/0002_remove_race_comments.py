# Generated by Django 4.2 on 2023-10-10 04:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("race", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="race",
            name="comments",
        ),
    ]
