# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-08-25 11:55
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectroRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.CharField(default=None, max_length=20)),
                ('team', models.CharField(default=None, max_length=20, unique=True)),
                ('fname', models.CharField(max_length=40)),
                ('fcollege', models.CharField(max_length=60)),
                ('fmail', models.EmailField(default=None, max_length=254, unique=True)),
                ('fcon', models.CharField(default=None, max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('fcity', models.CharField(max_length=12, null=True)),
                ('sname', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('scollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('smail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('scon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('scity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ManualroboRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.CharField(default=None, max_length=20)),
                ('team', models.CharField(default=None, max_length=20, unique=True)),
                ('fname', models.CharField(max_length=40)),
                ('fcollege', models.CharField(max_length=60)),
                ('fmail', models.EmailField(default=None, max_length=254, unique=True)),
                ('fcon', models.CharField(default=None, max_length=12, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('fcity', models.CharField(max_length=12, null=True)),
                ('sname', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('scollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('smail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('scon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('scity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('tname', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('tcollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('tmail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('tcon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('tcity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('foname', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('focollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('fomail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('focon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('focity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('finame', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('ficollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('fimail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('ficon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('ficity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SelfBalRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnum', models.CharField(default=None, max_length=20)),
                ('team', models.CharField(default=None, max_length=20, unique=True)),
                ('fname', models.CharField(max_length=40)),
                ('fcollege', models.CharField(max_length=60)),
                ('fmail', models.EmailField(default=None, max_length=254, unique=True)),
                ('fcon', models.CharField(default=None, max_length=12, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('fcity', models.CharField(max_length=12, null=True)),
                ('sname', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('scollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('smail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('scon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('scity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('tname', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('tcollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('tmail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('tcon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('tcity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('foname', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('focollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('fomail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('focon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('focity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('finame', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('ficollege', models.CharField(blank=True, default=None, max_length=60, null=True)),
                ('fimail', models.EmailField(blank=True, default=None, max_length=254, null=True)),
                ('ficon', models.CharField(blank=True, default=None, max_length=12, null=True, validators=[django.core.validators.RegexValidator('^[0-9]+$', 'Enter a valid phone number.')])),
                ('ficity', models.CharField(blank=True, default=None, max_length=12, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='bakerregistration',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]