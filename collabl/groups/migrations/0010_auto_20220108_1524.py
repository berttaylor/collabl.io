# Generated by Django 3.2.9 on 2022-01-08 15:24

from django.db import migrations, models
import collabl.storages


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0009_auto_20220107_0044"),
    ]

    operations = [
        migrations.DeleteModel(
            name="GroupProfileImage",
        ),
        migrations.AddField(
            model_name="group",
            name="profile_image",
            field=models.FileField(
                blank=True,
                help_text="Profile Image for the group. Please aim to keep this below 1mb in size.",
                null=True,
                upload_to=collabl.storages.group_based_upload_to,
            ),
        ),
    ]
