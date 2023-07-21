from django.db import models

# Create your models here.
class userRegistration(models.Model):
    id = models.AutoField
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=13)
    user_email = models.EmailField()
    user_password = models.CharField(max_length=100)
    # user_client_secret_json = models.FileField(upload_to='clientFile/secretFiles')
    # user_client_cobaltdeck_json = models.FileField(upload_to='clientFile/cobaltFiles')

    def __str__(self):
        return self.user_name