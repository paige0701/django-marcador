from django.conf.urls import url
from marcador import views

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='bookmark_user'),
    url(r'^$', views.bookmark_list, name='bookmark_list'),
]