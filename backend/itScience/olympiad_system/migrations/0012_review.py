# Generated by Django 2.2.7 on 2019-12-21 08:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('olympiad_system', '0011_solution_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField()),
                ('criteria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympiad_system.Criteria', verbose_name='Критерій')),
                ('solution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='olympiad_system.Solution', verbose_name="Розв'язок")),
            ],
            options={
                'unique_together': {('solution', 'criteria')},
            },
        ),
    ]