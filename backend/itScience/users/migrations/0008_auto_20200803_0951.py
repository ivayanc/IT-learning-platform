# Generated by Django 2.2.7 on 2020-08-03 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200803_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemuser',
            name='role',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.Role'),
        ),
    ]