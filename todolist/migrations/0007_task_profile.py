# Generated by Django 5.0.6 on 2024-08-20 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0006_task_atachment"),
        ("users", "0003_profile_delete_person"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="profile",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="users.profile",
            ),
            preserve_default=False,
        ),
    ]