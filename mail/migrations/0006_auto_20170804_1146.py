# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 06:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mail', '0005_auto_20170804_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mail',
            name='Sender',
            field=models.EmailField(max_length=254),
        ),
    ]
