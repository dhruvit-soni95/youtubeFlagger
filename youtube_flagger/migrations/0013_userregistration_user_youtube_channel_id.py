# Generated by Django 4.2.2 on 2023-07-26 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_flagger', '0012_alter_userregistration_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='userregistration',
            name='user_youtube_channel_id',
            field=models.CharField(default='', editable=False, max_length=50),
        ),
    ]
