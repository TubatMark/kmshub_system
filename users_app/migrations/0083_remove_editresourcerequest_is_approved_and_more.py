# Generated by Django 4.2.7 on 2024-02-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_app", "0082_remove_resources_is_pending_edit"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="editresourcerequest",
            name="is_approved",
        ),
        migrations.RemoveField(
            model_name="editresourcerequest",
            name="edited_cmi",
        ),
        migrations.RemoveField(
            model_name="editresourcerequest",
            name="edited_commodity",
        ),
        migrations.RemoveField(
            model_name="editresourcerequest",
            name="edited_knowledge",
        ),
        migrations.AddField(
            model_name="editresourcerequest",
            name="edited_cmi",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="editresourcerequest",
            name="edited_commodity",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="editresourcerequest",
            name="edited_knowledge",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
