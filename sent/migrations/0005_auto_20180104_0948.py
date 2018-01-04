# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sent', '0004_auto_20180104_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='message',
            field=models.CharField(verbose_name='description!!', max_length=512),
        ),
    ]
