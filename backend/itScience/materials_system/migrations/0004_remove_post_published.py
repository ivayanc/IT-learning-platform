# Generated by Django 2.2.7 on 2020-09-03 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materials_system', '0003_auto_20200903_2113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published',
        ),
    ]