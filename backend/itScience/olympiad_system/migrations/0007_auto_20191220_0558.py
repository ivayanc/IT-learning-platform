# Generated by Django 2.2.7 on 2019-12-20 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('olympiad_system', '0006_auto_20191220_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='solution_file',
            field=models.FileField(max_length='500', upload_to='solutions/', verbose_name="Файл розв'язок"),
        ),
    ]
