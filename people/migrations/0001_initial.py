# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-27 13:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=41)),
                ('description', models.TextField()),
                ('leader', models.CharField(max_length=41)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=31, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=41)),
                ('description', models.TextField()),
                ('festival_date', models.DateField(verbose_name='festival date')),
                ('colors', models.CharField(max_length=31)),
                ('slug', models.SlugField(max_length=31, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parishioner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=41)),
                ('date_of_birth', models.DateField(blank=True, verbose_name='date of birth')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('start_date', models.DateField(verbose_name='date posted')),
                ('slug', models.SlugField(max_length=31, unique=True)),
                ('communities', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='parishoners', to='people.Community')),
            ],
        ),
        migrations.CreateModel(
            name='Sacrament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=41)),
                ('description', models.TextField()),
                ('slug', models.SlugField(max_length=31, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=41)),
                ('description', models.TextField()),
                ('leader', models.CharField(max_length=41)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=31, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='parishioner',
            name='sacraments',
            field=models.ManyToManyField(blank=True, related_name='parishoners', to='people.Sacrament'),
        ),
        migrations.AddField(
            model_name='parishioner',
            name='societies',
            field=models.ManyToManyField(blank=True, related_name='parishoners', to='people.Society'),
        ),
    ]
