# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-04 06:14
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_auto_20170803_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='user',
        ),
        migrations.AlterField(
            model_name='mail',
            name='Sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]