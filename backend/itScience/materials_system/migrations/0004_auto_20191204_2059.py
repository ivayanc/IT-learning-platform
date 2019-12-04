# Generated by Django 2.2.7 on 2019-12-04 20:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('materials_system', '0003_post_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='full_title',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='short_title',
        ),
        migrations.AddField(
            model_name='post',
            name='moderator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='SchoolPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='materials_system.Post')),
            ],
        ),
        migrations.CreateModel(
            name='ProgrammingPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='materials_system.Post')),
            ],
        ),
        migrations.CreateModel(
            name='ItPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='materials_system.Post')),
            ],
        ),
    ]
