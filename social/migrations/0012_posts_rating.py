# Generated by Django 2.1.1 on 2018-10-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_auto_20181024_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='rating'),
        ),
    ]
