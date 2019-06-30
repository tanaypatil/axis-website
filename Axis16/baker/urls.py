from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$', views.logindisp, name='logindisp'),
               url(r'^login2', views.login2, name='login2'),
               url(r'^ques.html$', views.ques, name='ques'),
               url(r'^check', views.check, name='check'),
               url(r'^sofar.html$', views.sofar, name='sofar'),
]
