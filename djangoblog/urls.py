"""djangoblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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

import xadmin
import DjangoUeditor
import os
from django.conf.urls.static import static
from djangoblog import settings
from django.views.static import serve
from users.views import RegisterView, LoginView, LogoutView, ActiveView
from blogs.views import IndexView
from djangoblog.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),

    url(r'^index/$', IndexView.as_view(), name='index'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^active/(?P<active_code>\w+)/$', ActiveView.as_view(), name='active'),

    url(r'^blog/', include('blogs.urls', namespace='blog')),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]

if settings.DEBUG:
    media_root = os.path.join(settings.BASE_DIR, settings.MEDIA_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=media_root)
