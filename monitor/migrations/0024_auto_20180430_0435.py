# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0023_auto_20180430_0435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serverdisk',
            name='disk',
            field=models.CharField(max_length=120),
        ),
    ]
