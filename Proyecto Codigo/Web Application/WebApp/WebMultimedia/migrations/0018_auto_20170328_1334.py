# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-28 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebMultimedia', '0017_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfiluser',
            name='direccion',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='perfiluser',
            name='edad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='perfiluser',
            name='pais',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='perfiluser',
            name='provincia',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='perfiluser',
            name='sexo',
            field=models.CharField(max_length=10, null=True),
        ),
    ]