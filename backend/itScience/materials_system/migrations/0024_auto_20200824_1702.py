# Generated by Django 2.2.7 on 2020-08-24 14:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materials_system', '0023_auto_20200820_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='Дата написання коментаря'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='reply_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='materials_system.Comments', verbose_name='Вiдповiдь на'),
        ),
    ]
