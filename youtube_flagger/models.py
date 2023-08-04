from django.db import models

# Create your models here.
class userRegistration(models.Model):
    id = models.AutoField
    user_name = models.CharField("Enter your Name",max_length=50)
    user_phone = models.CharField("Enter Phone Number",max_length=13)
    user_email = models.EmailField("Enter Email")
    user_password = models.CharField("Enter Password",max_length=100)
    user_youtube_channel_id = models.CharField("Enter your Youtube Channel Id", max_length=50)
    user_client_secret_json = models.FileField()
    user_client_cobaltdeck_json = models.FileField()

    def __str__(self):
        return self.user_name



