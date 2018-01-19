from django.conf.urls import url, include
from musa import views


from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.homepage, name ='home'),
    url(r'^about/$', views.aboutpage, name ='about'),
    url(r'^download/$', views.downloadpage, name ='download'),
    url(r'^contact/$', views.contactpage, name ='contact'),
    
   
    
    url(r'^welcome/$', views.userpage, name ='welcome'),
    url(r'^download_app/musiana.tar.gz$',views.downloadapp,),
    url(r'^playlist/$', views.playlist, name='playlist'),

   #registration redux
    url(r'^accounts/', include('registration.backends.simple.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
