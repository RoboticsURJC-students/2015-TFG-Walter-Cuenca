# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 14:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMultimedia', '0018_auto_20170328_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiluser',
            name='perfilImg',
            field=models.ImageField(blank=True, default='img_perfil/perfilFault.jpeg', null=True, upload_to='img_perfil/'),
        ),
    ]
