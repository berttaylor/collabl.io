# Generated by Django 3.2.9 on 2022-01-18 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborations', '0007_collaborationtask_prompt_for_details_on_completion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollaborationFile',
        ),
    ]
