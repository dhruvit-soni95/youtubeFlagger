# Generated by Django 4.2.2 on 2023-08-18 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_flagger', '0017_rename_user_client_cobaltdeck_json_userregistration_user_client_service_account_json_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='Advisor_id',
            field=models.CharField(default='', max_length=50),
        ),
    ]