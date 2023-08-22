from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

# from cmnt_flagger.youtube_flagger.models import userRegistration
# from cmnt_flagger.youtube_flagger.models import userRegistration
# from cmnt_flagger.youtube_flagger.models import userRegistration

import os, sys
da = sys.path.append("../../cmnt_flagger/youtube_flagger/models.py")
# os.environ['DJANGO_SETTINGS_MODULE'] = "cmnt_flagger.settings"
# from cmnt_flagger.youtube_flagger import models

# Create your views here.
def home(request):
    return render(request, "home.html")


def inviterequest(request, user_id):
    ok = da.userRegistration
    invited_user_id = user_id
    mydata = ok.objects.get(id=invited_user_id)
    return render(request, "success_invitation_message.html", {"user_id": mydata.user_email})