# Generated by Django 2.2.7 on 2019-12-20 05:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('olympiad_system', '0005_task_task_alias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='legend',
        ),
        migrations.AddField(
            model_name='solution',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solution',
            name='solution_file',
            field=models.FileField(upload_to='solutions/', verbose_name="Файл розв'язок"),
        ),
    ]