from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^$', 'sapp.views.login' ,name="index"),
    url(r'^home/$', 'sapp.views.home'),
    url(r'^logoff/$', 'sapp.views.logout'),
     url(r'^signup/$', 'sapp.views.signup'),


)
