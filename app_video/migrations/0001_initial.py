# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=500)),
                ('Descricao', models.CharField(max_length=500)),
                ('link', models.CharField(max_length=500)),
            ],
        ),
    ]
