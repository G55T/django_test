# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sent', '0007_posting_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
