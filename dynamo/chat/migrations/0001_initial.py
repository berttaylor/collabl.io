# Generated by Django 3.2.9 on 2021-11-21 12:25

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True,
                        help_text="Timestamp of when this object was first created.",
                        null=True,
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True,
                        help_text="Timestamp of when this object was last updated.",
                        null=True,
                    ),
                ),
                (
                    "deleted_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamp of when (if) this object was soft deleted.",
                        null=True,
                    ),
                ),
                ("message", models.TextField(help_text="The message itself")),
            ],
            options={
                "verbose_name_plural": "Chat Messages",
                "ordering": ["-created_at"],
            },
        ),
    ]
