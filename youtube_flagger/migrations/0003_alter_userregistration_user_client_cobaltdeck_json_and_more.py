# Generated by Django 4.2.2 on 2023-07-19 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_flagger', '0002_userregistration_user_client_cobaltdeck_json_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userregistration',
            name='user_client_cobaltdeck_json',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='user_client_secret_json',
            field=models.CharField(default='', max_length=200),
        ),
    ]
