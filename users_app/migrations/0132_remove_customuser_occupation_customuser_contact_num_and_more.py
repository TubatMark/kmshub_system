# Generated by Django 4.2.7 on 2024-04-30 01:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users_app", "0131_alter_cmi_longitude_alter_commodity_longitude_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="occupation",
        ),
        migrations.AddField(
            model_name="customuser",
            name="contact_num",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="date_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="gender",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="highest_educ",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="sex",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="specialization",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
