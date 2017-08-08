
from django.conf.urls import url
from . import views 

urlpatterns = [
    url(r'^mail/$', views.home ,name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signout1/$', views.signout, name='signout'),
    url(r'^sendingmail/$', views.send_email, name='send_email'),
    url(r'^inbox/$', views.inbox, name='inbox'),
    url(r'^mail_remove/(?P<pk>\d+)/(?P<delete_id>\d+)/$', views.mail_remove, name='mail_remove'),
]
