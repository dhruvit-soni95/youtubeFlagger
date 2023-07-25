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
        fields = ('__all__')

    def __int__(self, *args, **kwargs):
        super(userRegistration, self).__init__(*args, **kwargs)
        for fiels_name, field in self.fields.items():
            field.widget.attrs['class'] = 'row'
