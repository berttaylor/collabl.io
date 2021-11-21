# Generated by Django 3.2.9 on 2021-11-21 12:25

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
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
                (
                    "name",
                    models.CharField(
                        help_text="A name for the group e.g. 'Riverdale Parents Group'",
                        max_length=100,
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True,
                        help_text="Auto-generated slug for the Group",
                        max_length=150,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="A description of the group and it's causes",
                        max_length=500,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Groups",
            },
        ),
        migrations.CreateModel(
            name="GroupProfileImage",
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
                (
                    "alt_text",
                    models.CharField(
                        help_text="The full alt text of the image for accessibility purposes.",
                        max_length=100,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Profile Images",
            },
        ),
        migrations.CreateModel(
            name="GroupJoinRequest",
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
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Pending", "Pending"),
                            ("Approved", "Approved"),
                            ("Denied", "Denied"),
                        ],
                        default="Pending",
                        help_text="The status of the request",
                        max_length=100,
                    ),
                ),
                (
                    "handled_date",
                    models.DateTimeField(
                        blank=True,
                        help_text="Timestamped when the request is handled",
                        null=True,
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        help_text="The Group which the User would like to join",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="join_requests",
                        to="groups.group",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Join Requests",
            },
        ),
    ]
