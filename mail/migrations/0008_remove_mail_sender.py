# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 05:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0007_auto_20170808_1009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mail',
            name='Sender',
        ),
    ]
