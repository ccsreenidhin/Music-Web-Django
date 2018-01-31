from django.conf.urls import url, include
from musa import views


from django.conf import settings

from django.conf.urls.static import static




urlpatterns = [
    url(r'^$', views.homepage, name ='home'),
    url(r'^about/$', views.aboutpage, name ='about'),
    url(r'^download/$', views.downloadpage, name ='download'),
    url(r'^contact/$', views.contactpage, name ='contact'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^download_app/musiana.tar.gz$',views.downloadapp,),
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^welcome/$', views.userpage, name ='welcome'),
    url(r'^profile/$', views.profileview, name ='profile'),
    url(r'^delete/(?P<pk>\d+)/$', views.musicdelete, name='mdelete'),
    url(r'^profedit/$', views.profedit, name='pedit'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
