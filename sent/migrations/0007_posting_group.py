# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sent', '0006_auto_20180104_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='posting',
            name='group',
            field=models.CharField(verbose_name='group', max_length=2, default=0),
            preserve_default=False,
        ),
    ]
