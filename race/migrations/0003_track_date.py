# Generated by Django 4.2 on 2023-10-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("race", "0002_remove_race_comments"),
    ]

    operations = [
        migrations.AddField(
            model_name="track",
            name="date",
            field=models.DateField(null=True),
        ),
    ]
