# Generated by Django 2.2.7 on 2020-08-03 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_roles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
    ]