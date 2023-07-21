from django import forms
from .models import userRegistration

# class FileUploadForm(forms.ModelForm):
#     class Meta:
#         model = userRegistration
#         fields = ('user_name','user_phone','user_email','user_password','user_client_secret_json','user_client_cobaltdeck_json')
#
class JSONUploadForm(forms.ModelForm):
    class Meta:
        model = userRegistration
        fields = ('user_name','user_phone','user_email','user_password')
