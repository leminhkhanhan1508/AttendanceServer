# Generated by Django 3.1.4 on 2021-01-07 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0004_auto_20210107_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.URLField(),
        ),
    ]
