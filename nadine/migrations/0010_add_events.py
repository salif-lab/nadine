# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-14 18:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import nadine.models.resource


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nadine', '0009_auto_20160908_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_ts', models.DateTimeField(auto_now_add=True)),
                ('start_ts', models.DateTimeField(verbose_name=b'Start time')),
                ('end_ts', models.DateTimeField(verbose_name=b'End time')),
                ('description', models.CharField(max_length=128, null=True)),
                ('charge', models.DecimalField(decimal_places=2, max_digits=9)),
                ('is_public', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('location', models.CharField(max_length=128, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('floor', models.SmallIntegerField()),
                ('seats', models.SmallIntegerField()),
                ('max_capacity', models.SmallIntegerField()),
                ('has_av', models.BooleanField(default=False)),
                ('has_phone', models.BooleanField(default=False)),
                ('default_rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('image', models.ImageField(blank=True, null=True, upload_to=nadine.models.resource.room_img_upload_to)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nadine.Room'),
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]