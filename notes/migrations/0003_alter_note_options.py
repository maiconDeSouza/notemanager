# Generated by Django 5.1 on 2024-08-25 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_alter_note_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-important', 'created_at']},
        ),
    ]
