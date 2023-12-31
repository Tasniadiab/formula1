# Generated by Django 4.2 on 2023-10-10 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("country", models.CharField(max_length=250)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("country", models.CharField(max_length=250)),
                ("team_principle", models.CharField(max_length=250)),
                (
                    "place_in_championship",
                    models.SmallIntegerField(blank=True, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Track",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("location", models.CharField(max_length=250)),
                ("url", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Race",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("grid", models.IntegerField()),
                ("date", models.DateField()),
                ("comments", models.TextField()),
                (
                    "driver",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="race.driver"
                    ),
                ),
                (
                    "track",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="race.track"
                    ),
                ),
            ],
            options={
                "ordering": ["date"],
            },
        ),
        migrations.AddField(
            model_name="driver",
            name="races",
            field=models.ManyToManyField(through="race.Race", to="race.track"),
        ),
        migrations.AddField(
            model_name="driver",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="drivers_team",
                to="race.team",
            ),
        ),
    ]
