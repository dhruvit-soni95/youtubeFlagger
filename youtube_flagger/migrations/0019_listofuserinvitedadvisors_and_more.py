# Generated by Django 4.2.2 on 2023-08-18 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_flagger', '0018_userregistration_advisor_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='listofUserInvitedAdvisors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('invited_friends_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='userregistration',
            name='Advisor_id',
            field=models.CharField(max_length=50),
        ),
    ]