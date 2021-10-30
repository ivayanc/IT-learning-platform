# Generated by Django 2.2.7 on 2020-05-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympiad_system', '0013_auto_20191221_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Очікується перевірка'), (2, 'Відбувається перевірка'), (3, 'Перевірка завершена')], default=1, verbose_name='Статус перевірки'),
        ),
    ]