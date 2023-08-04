from django.apps import AppConfig
# from apscheduler.schedulers.background import BackgroundScheduler
# from .files.tasks import my_periodic_task
# from .views import main
# from urllib3 import request

class YoutubeFlaggerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'youtube_flagger'
    # def ready(self):
    #     scheduler = BackgroundScheduler()
    #     scheduler.add_job(my_periodic_task(), 'interval', seconds=10)  # Adjust the interval as per your requirements
    #     scheduler.start()