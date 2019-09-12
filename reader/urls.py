from django.conf.urls import url
from reader import views

app_name = 'reader'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^gettoken/$', views.gettoken, name='gettoken'),
    url(r'^mail/$', views.mail, name='mail'),
]
