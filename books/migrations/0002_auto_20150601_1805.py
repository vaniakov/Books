# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biba',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('boba', models.CharField(max_length=12)),
            ],
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='author',
            name='email',
            field=models.EmailField(max_length=254, verbose_name=b'e-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
