from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('youtube', views.youtube, name="youtube"),
    path('fetchedvideos', views.fetchYTvideos, name="fetchYTvideos"),
    path('retrieveComments', views.retrieveComments, name="retrieveComments"),
    path('processing', views.processing, name="processing"),
    path('main', views.main, name="main"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
