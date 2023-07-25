import os
from django.conf import settings


def handle_uploaded_file(f):
    cobalt_path = os.path.join(settings.SECRETS_DIR, 'upload/')
    with open(cobalt_path+f.name, 'wb+') as destination:
    # with open('youtube_flagger/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)