# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-16 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMultimedia', '0022_auto_20170328_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cantante',
            name='inf',
            field=models.TextField(),
        ),
    ]
