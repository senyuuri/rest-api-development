"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path
from apiapp import views

urlpatterns = [
    re_path(r'^$', views.endpoints),
    re_path(r'^meta/heartbeat$', views.heartbeat),
    re_path(r'^meta/members$', views.user_list),
    re_path(r'^users/register$', views.user_register),
    re_path(r'^users/authenticate$', views.user_auth),
    re_path(r'^users/expire$', views.token_exp),
    re_path(r'^users/$', views.user_detail),
    re_path(r'^diary/$', views.list_diaries),
    re_path(r'^diary/create/$', views.create_diary),
    re_path(r'^diary/delete/$', views.delete_diary),
    re_path(r'^diary/permission/$', views.update_diary),
]
