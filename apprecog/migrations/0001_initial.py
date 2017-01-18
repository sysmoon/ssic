# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('listIdx', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('appName', models.CharField(max_length=30)),
                ('sppServerity', models.CharField(max_length=10)),
                ('corpName', models.CharField(max_length=50)),
                ('summary', models.CharField(max_length=255)),
                ('readCnt', models.PositiveIntegerField()),
                ('regId', models.CharField(max_length=50)),
                ('regDate', models.DateField()),
                ('updId', models.CharField(max_length=50)),
                ('updDate', models.DateField()),
                ('delFlag', models.CharField(max_length=1)),
                ('pubDate', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
