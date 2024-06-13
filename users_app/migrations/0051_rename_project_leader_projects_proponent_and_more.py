# Generated by Django 4.2.7 on 2024-01-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_app", "0050_projects_project_file"),
    ]

    operations = [
        migrations.RenameField(
            model_name="projects",
            old_name="project_leader",
            new_name="proponent",
        ),
        migrations.RenameField(
            model_name="projects",
            old_name="project_description",
            new_name="summary",
        ),
        migrations.AddField(
            model_name="projects",
            name="number_years",
            field=models.IntegerField(default=0),
        ),
    ]
