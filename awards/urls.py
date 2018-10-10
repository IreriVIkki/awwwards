
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^userdetails/$', views.profile, name='profile'),
    url(r'^signup/$', views.signup, name='signup'),
]
