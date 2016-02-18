# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('genero', models.CharField(max_length=1, choices=[('F', 'Felino'), ('C', 'Canino'), ('R', 'Réptil')])),
                ('raca', models.CharField(max_length=20)),
                ('cor', models.CharField(max_length=20)),
                ('porte', models.CharField(max_length=1, choices=[('P', 'Pequeno'), ('M', 'Médio'), ('G', 'Grande')])),
                ('dono', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
