# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-30 13:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Artical',
            new_name='Articles',
        ),
    ]
