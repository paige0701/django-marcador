from django.conf.urls import url
from marcador import views
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.views import login as login
from django.contrib.auth.views import logout as logout

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='bookmark_user'),
    url(r'^$', views.bookmark_list, name='bookmark_list'),

    url(r'^create/$', views.bookmark_create, name='bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.bookmark_edit, name = 'bookmark_edit'),

    # url(r'^create/$', 'marcador.views.bookmark_create',
    #     name='marcador_bookmark_create'),
    # url(r'^edit/(?P<pk>\d+)/$', 'marcador.views.bookmark_edit',
    #     name='marcador_bookmark_edit'),
    #

    url(r'^login/$', login, {'template_name':"login.html"}, name='mysite_login'),
    url(r'^logout/$', logout, {'next_page': reverse_lazy('bookmark_list')}, name='mysite_logout'),






    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
    #     name='mysite_login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout',
    #     {'next_page': reverse_lazy('marcador_bookmark_list')}, name='mysite_logout'),



]