# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('listIdx', models.AutoField(serialize=False, primary_key=True)),
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
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
