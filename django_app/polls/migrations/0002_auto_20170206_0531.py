# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 05:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='q_text',
            new_name='question_text',
        ),
    ]
