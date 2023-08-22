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
    path('comments', views.comments, name='comments'),
    path('profile', views.profile, name='profile'),
    path('invitefriend', views.invitefriend, name='invitefriend'),

    # path('home', views.home, name="home"),
    path('request/<user_id>/<friends_email>', views.inviterequest, name="request"),
    path('getdatawhoinvited', views.getdatawhoinvited, name="getdatawhoinvited"),
    path('seeDetails/<id>', views.seeUserDetails, name="seeDetails"),
    path('seeDetails/seeUserComments/<id>', views.seeUserComments, name="seeUserComments"),
    path('seeDetails/users_held_for_review_comments/<id>', views.users_held_for_review_comments, name="users_held_for_review_comments"),
    path('seeDetails/seeUserComments/users_checkHeldforReview/<id>', views.users_checkHeldforReview, name="users_checkHeldforReview"),
    path('seeDetails/users_held_for_review_comments/users_checkPublished/<id>', views.users_checkPublished, name="users_checkPublished"),
    path('seeDetails/seeUserComments/users_perticulardeleteYTcomment/<video_Id>/<commentsss>/<id>', views.users_perticulardeleteYTcomment, name="users_perticulardeleteYTcomment"),
    path('seeDetails/seeUserComments/users_replyYTcomment/<comment_Id>/<comment_text>/<id>', views.users_replyYTcomment, name="users_replyYTcomment"),
    path('seeDetails/users_main/<id>', views.users_main, name="users_main"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
