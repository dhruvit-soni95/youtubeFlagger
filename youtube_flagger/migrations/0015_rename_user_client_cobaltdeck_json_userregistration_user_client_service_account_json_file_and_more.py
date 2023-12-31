# Generated by Django 4.2.2 on 2023-08-10 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_flagger', '0014_alter_userregistration_user_youtube_channel_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userregistration',
            old_name='user_client_cobaltdeck_json',
            new_name='user_client_service_account_json_file',
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='user_youtube_channel_id',
            field=models.CharField(max_length=50, verbose_name='Enter your Youtube Channel Id'),
        ),
    ]
