# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sent', '0003_auto_20180104_0259'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='title',
            field=models.CharField(max_length=64, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='posting',
            name='created_at',
            field=models.DateTimeField(verbose_name='date', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='posting',
            name='message',
            field=models.CharField(verbose_name='description', max_length=512),
        ),
    ]
