# Generated by Django 4.2.20 on 2025-03-24 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="profile_picture",
            field=models.ImageField(
                blank=True, null=True, upload_to="profile/patient/images"
            ),
        ),
    ]
