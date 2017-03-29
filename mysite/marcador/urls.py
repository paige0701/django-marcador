from django.conf.urls import url
from marcador import views
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.views import login as login
from django.contrib.auth.views import logout as logout

urlpatterns = [
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='bookmark_user'),
    url(r'^$', views.bookmark_list, name='bookmark_list'),

    url(r'^login/$', login, {'template_name':"login.html"}, name='mysite_login'),
    url(r'^logout/$', logout, {'next_page': reverse_lazy('bookmark_list')}, name='mysite_logout'),






    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
    #     name='mysite_login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout',
    #     {'next_page': reverse_lazy('marcador_bookmark_list')}, name='mysite_logout'),



]