# Generated by Django 2.1.1 on 2018-10-14 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userintrests',
            name='intrest',
            field=models.CharField(max_length=10),
        ),
    ]
