# Generated by Django 3.1.5 on 2021-01-24 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0019_auto_20210122_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendent',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendent',
            name='report',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendent',
            name='url_image',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
