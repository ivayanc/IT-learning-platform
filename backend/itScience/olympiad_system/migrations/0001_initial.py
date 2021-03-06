# Generated by Django 2.2.7 on 2019-12-20 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descrition', models.CharField(max_length=256, verbose_name='Опис критерія')),
                ('max_value', models.IntegerField(verbose_name='Максимальний бал')),
                ('step', models.FloatField(verbose_name='Крок оцінки')),
            ],
        ),
        migrations.CreateModel(
            name='Olympiad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Дата почтку')),
                ('title', models.CharField(max_length=256, verbose_name='Назва олімпіади')),
                ('duration', models.DurationField(verbose_name='Час проведення')),
                ('description', models.TextField(verbose_name='Опис олімпіади')),
                ('olymp_type', models.PositiveSmallIntegerField(choices=[(1, 'Відкрита'), (2, 'За запрошенням')], default=1, verbose_name='Тип проведення')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('solution_file', models.FileField(upload_to='', verbose_name="Файл розв'язок")),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Назва задачі')),
                ('description', models.TextField(verbose_name='Опис задачі')),
                ('files', models.FileField(blank=True, upload_to='', verbose_name='Додаткові матеріали')),
                ('task_type', models.PositiveSmallIntegerField(choices=[(1, 'Excel'), (2, 'Access'), (3, 'Word'), (4, 'PowerPoint'), (5, 'Інше')], default=5, verbose_name='Розділ задачі')),
                ('olympiad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympiad_system.Olympiad', verbose_name='Олімпіада')),
            ],
        ),
    ]
