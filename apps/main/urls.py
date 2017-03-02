from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register_user$', views.register),
    url(r'^login_user$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add_friend/(?P<id>\d+)/$', views.add_friend),
    url(r'^view_profile/(?P<id>\d+)/$', views.view_profile),
    url(r'^remove_friend/(?P<id>\d+)/$', views.remove),
    url(r'^dashboard$',views.dashboard),
]
