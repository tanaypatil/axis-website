# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 17:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_bakerregistration_lastsubmit'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bakerregistration',
            options={'ordering': ['-level', 'lastSubmit']},
        ),
    ]
