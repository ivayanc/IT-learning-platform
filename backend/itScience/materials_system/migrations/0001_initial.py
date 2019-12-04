# Generated by Django 2.2.7 on 2019-12-04 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=150)),
                ('full_title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=500)),
                ('published', models.DateTimeField(auto_now=True)),
                ('title_image', models.ImageField(upload_to='static/post_images/')),
                ('publication', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('about', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='PostHashTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials_system.Post')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materials_system.HashTag')),
            ],
        ),
    ]
