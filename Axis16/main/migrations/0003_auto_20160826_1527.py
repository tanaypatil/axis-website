# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-08-26 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160825_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bakerregistration',
            options={'ordering': ['-level']},
        ),
    ]
