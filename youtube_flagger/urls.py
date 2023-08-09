from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('index', views.index, name="index"),
    path('youtube', views.youtube, name="youtube"),
    path('fetchedvideos', views.fetchYTvideos, name="fetchYTvideos"),
    path('checkHeldforReview', views.checkHeldforReview, name="checkHeldforReview"),
    path('perticulardeleteYTcomment/<video_Id>/<commentsss>', views.perticulardeleteYTcomment, name="perticulardeleteYTcomment"),
    path('checkPublished', views.checkPublished, name="checkPublished"),
    path('secondmain', views.secondmain, name="secondmain"),
    path('retrieveComments', views.retrieveComments, name="retrieveComments"),
    path('processing', views.processing, name="processing"),
    path('main', views.main, name="main"),
    path('AutoScanYT', views.AutoScanYT, name="AutoScanYT"),

    # path('getvideoAndComment', views.getvideoAndComment, name="getvideoAndComment"),

    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('registration', views.registration, name="registration"),
    path('downloadpdf/', views.download_pdf, name='download_pdf'),
    path('replycomment/<comment_Id>/<comment_text>', views.replyYTcomment, name="replyYTcomment"),
    # path('checking', views.perform_question_answering, name="perform_question_answering"),
    path('payment', views.payment, name='payment'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
