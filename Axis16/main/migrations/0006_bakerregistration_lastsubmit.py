# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160907_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='bakerregistration',
            name='lastSubmit',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]
