# Generated by Django 4.2.7 on 2024-03-13 03:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_app", "0106_uploadvideo"),
    ]

    operations = [
        migrations.AddField(
            model_name="editresourcerequest",
            name="date_updated",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
