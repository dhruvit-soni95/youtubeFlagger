# Generated by Django 4.2.2 on 2023-07-21 03:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_flagger', '0005_alter_userregistration_user_client_cobaltdeck_json_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userregistration',
            name='user_client_cobaltdeck_json',
        ),
    ]
