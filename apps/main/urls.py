from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_user$', views.register),
    url(r'^login_user$', views.login),
    url(r'^logout$', views.logout),
    url(r'^dashboard$',views.dashboard),
]
