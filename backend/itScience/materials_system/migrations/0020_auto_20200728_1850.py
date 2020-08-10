# Generated by Django 2.2.7 on 2020-07-28 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materials_system', '0019_remove_hashtag_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='tag_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='hashtag',
            unique_together=set(),
        ),
    ]