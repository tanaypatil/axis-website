"""Axis16 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from android import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^predator/', admin.site.urls),
    url(r'^', include('main.urls')),
    # url(r'^baker/', include('baker.urls')),
    url(r'^androregs', views.RegList.as_view()),
    url(r'^msgandro', views.FeedList.as_view()),
    url(r'^notifsandro', views.Notifs.as_view()),
    url(r'^regandro', views.amishreg),
    url(r'^getnotifs', views.getnotifs),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)

admin.site.site_header = 'AXIS 2016'
admin.site.site_title = 'AXIS ADMINS'
admin.site.index_title = 'AXIS ADMINISTRATION'
