# Generated by Django 2.2.7 on 2020-05-29 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials_system', '0017_auto_20200528_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='test',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
