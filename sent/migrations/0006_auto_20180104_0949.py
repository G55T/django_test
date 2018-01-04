# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sent', '0005_auto_20180104_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='message',
            field=models.CharField(verbose_name='description', max_length=512),
        ),
        migrations.AlterField(
            model_name='posting',
            name='title',
            field=models.CharField(verbose_name='title', max_length=64),
        ),
    ]
