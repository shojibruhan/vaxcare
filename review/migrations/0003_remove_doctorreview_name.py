# Generated by Django 4.2.20 on 2025-03-30 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("review", "0002_campaignreview_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="doctorreview", name="name",),
    ]
