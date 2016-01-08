# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0009_community_description'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='community',
            managers=[
                ('default', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='community',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]