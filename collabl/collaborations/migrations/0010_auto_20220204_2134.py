# Generated by Django 3.2.9 on 2022-02-04 21:34

import collaborations.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("collaborations", "0009_auto_20220122_1158"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="collaboration",
            options={
                "ordering": ["-created_at"],
                "verbose_name_plural": "Collaborations",
            },
        ),
        migrations.AlterField(
            model_name="collaboration",
            name="created_by",
            field=models.ForeignKey(
                help_text="User who created the collaboration",
                on_delete=models.SET(collaborations.models.get_sentinel_user),
                related_name="collaborations_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="collaborationtask",
            name="assigned_to",
            field=models.ForeignKey(
                blank=True,
                help_text="User who should complete the task",
                null=True,
                on_delete=models.SET(collaborations.models.get_sentinel_user),
                related_name="tasks_assigned",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="collaborationtask",
            name="completed_by",
            field=models.ForeignKey(
                blank=True,
                help_text="User who completed the task/reached the milestone",
                null=True,
                on_delete=models.SET(collaborations.models.get_sentinel_user),
                related_name="tasks_completed",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
