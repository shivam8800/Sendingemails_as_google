# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 04:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0006_auto_20170804_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mail',
            name='Sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_login_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
