# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 03:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0012_auto_20170418_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='clusters',
            name='indexer_algorithm',
            field=models.CharField(default='inception', max_length=50),
            preserve_default=False,
        ),
    ]
