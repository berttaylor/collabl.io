# Generated by Django 3.2.9 on 2021-11-21 12:25

import django.db.models.deletion
import users.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("groups", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="groupjoinrequest",
            name="handled_by",
            field=models.ForeignKey(
                blank=True,
                help_text="User who handled the request",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="group_join_requests_handled",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="groupjoinrequest",
            name="user",
            field=models.ForeignKey(
                help_text="The User who made the request",
                on_delete=models.SET(users.utils.get_sentinel_user),
                related_name="group_join_requests_made",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="admins",
            field=models.ManyToManyField(
                blank=True,
                help_text="Users with Administrative Rights",
                related_name="admin_positions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="created_by",
            field=models.ForeignKey(
                blank=True,
                help_text="User who created the group",
                on_delete=models.SET(users.utils.get_sentinel_user),
                related_name="groups_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="members",
            field=models.ManyToManyField(
                blank=True,
                help_text="Users who are members of the Group",
                related_name="memberships",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="group",
            name="subscribers",
            field=models.ManyToManyField(
                blank=True,
                help_text="Users who receive email updates from the Group",
                related_name="subscriptions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="groupjoinrequest",
            unique_together={("user", "group")},
        ),
        migrations.AddIndex(
            model_name="group",
            index=models.Index(
                fields=["created_at"], name="groups_grou_created_b17bf8_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="group",
            index=models.Index(fields=["name"], name="groups_grou_name_0806de_idx"),
        ),
        migrations.AddIndex(
            model_name="group",
            index=models.Index(fields=["slug"], name="groups_grou_slug_246a6a_idx"),
        ),
    ]