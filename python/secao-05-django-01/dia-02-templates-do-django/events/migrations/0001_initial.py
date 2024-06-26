# Generated by Django 4.2.5 on 2023-10-05 23:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("date", models.DateField()),
                ("location", models.CharField(max_length=200)),
                (
                    "event_type",
                    models.CharField(
                        choices=[
                            ("C", "Conference"),
                            ("S", "Seminar"),
                            ("W", "Workshop"),
                            ("O", "Other"),
                        ],
                        max_length=50,
                    ),
                ),
                ("is_remote", models.BooleanField(default=False)),
                ("image", models.ImageField(blank=True, upload_to="events/img")),
            ],
        ),
    ]
