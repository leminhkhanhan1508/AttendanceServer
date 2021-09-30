# Generated by Django 3.1.5 on 2021-05-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('First_App', '0025_user_user_id_card'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id_card',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]