# Generated by Django 3.2.9 on 2022-01-22 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborations', '0008_delete_collaborationfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collaborationtask',
            name='tags',
        ),
        migrations.DeleteModel(
            name='CollaborationTaskTag',
        ),
    ]
