from django.contrib import admin
from .models import userRegistration,listofUserInvitedAdvisors
# Register your models here.
admin.site.register(userRegistration)
admin.site.register(listofUserInvitedAdvisors)