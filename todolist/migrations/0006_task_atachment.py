# Generated by Django 5.0.6 on 2024-08-20 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todolist", "0005_alter_task_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="atachment",
            field=models.FileField(blank=True, null=True, upload_to="media/"),
        ),
    ]
