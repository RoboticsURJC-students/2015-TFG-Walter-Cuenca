# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-18 23:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fileCancion', models.FileField(upload_to='canciones/')),
            ],
        ),
        migrations.CreateModel(
            name='Cantante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('imgCantante', models.ImageField(upload_to='img_Cantante/')),
                ('nacionalidad', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('tipoArtista', models.CharField(max_length=200)),
                ('inf', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameProduct', models.CharField(max_length=200)),
                ('typeProduct', models.CharField(max_length=100)),
                ('typeTicket', models.CharField(blank=True, max_length=50)),
                ('cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contacta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('telefono', models.IntegerField()),
                ('motivo', models.CharField(choices=[('Eventos', 'Eventos'), ('Entrada', 'Entrada'), ('Tecnico', 'Tecnico'), ('Otro', 'Otro')], max_length=8)),
                ('texto', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('imgDisco', models.ImageField(upload_to='img_disco/')),
                ('listCanciones', models.ManyToManyField(to='WebMultimedia.Cancion')),
            ],
        ),
        migrations.CreateModel(
            name='Entradas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeEntrada', models.CharField(choices=[('Estandar', 'Estandar'), ('Vip 1', 'Vip 1'), ('Vip 2', 'Vip 2')], max_length=8)),
                ('precio', models.IntegerField()),
                ('descrip', models.CharField(max_length=200)),
                ('stock', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('imgCartel', models.ImageField(upload_to='img_Cartel/')),
                ('fecha', models.DateTimeField(verbose_name='fecha concierto')),
                ('pais', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('lugar', models.CharField(max_length=200)),
                ('listEntradas', models.ManyToManyField(to='WebMultimedia.Entradas')),
            ],
        ),
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fileImg', models.ImageField(upload_to='img_galeria/')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perfilImg', models.ImageField(null=True, upload_to='img_perfil')),
                ('telefono', models.IntegerField(null=True)),
                ('listCompra', models.ManyToManyField(to='WebMultimedia.Compra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('typeFile', models.CharField(choices=[('iframe', 'iframe'), ('video', 'video')], max_length=6)),
                ('fileVideo', models.FileField(blank=True, max_length=200, upload_to='videos/')),
                ('urlVideo', models.URLField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='evento',
            name='listVideos',
            field=models.ManyToManyField(to='WebMultimedia.Video'),
        ),
        migrations.AddField(
            model_name='evento',
            name='listcantantes',
            field=models.ManyToManyField(to='WebMultimedia.Cantante'),
        ),
        migrations.AddField(
            model_name='cantante',
            name='listDiscos',
            field=models.ManyToManyField(to='WebMultimedia.Disco'),
        ),
        migrations.AddField(
            model_name='cantante',
            name='listImagenes',
            field=models.ManyToManyField(to='WebMultimedia.Galeria'),
        ),
        migrations.AddField(
            model_name='cantante',
            name='listVideos',
            field=models.ManyToManyField(to='WebMultimedia.Video'),
        ),
        migrations.AddField(
            model_name='cancion',
            name='buyUser',
            field=models.ManyToManyField(to='WebMultimedia.PerfilUser'),
        ),
    ]
