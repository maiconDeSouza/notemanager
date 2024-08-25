# Generated by Django 5.1 on 2024-08-25 14:13

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('title', models.CharField(max_length=100, verbose_name='Título')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Descrição')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Criado em')),
                ('important', models.BooleanField(default=False, verbose_name='Importante')),
            ],
        ),
    ]
