# Generated by Django 2.2.7 on 2020-08-24 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials_system', '0026_auto_20200824_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='date',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='reply_to',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='text',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
    ]
