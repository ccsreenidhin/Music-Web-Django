from django.conf.urls import url
from musa import views


from django.conf import settings

from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.homepage, name ='home'),
    url(r'^about/$', views.aboutpage, name ='about'),
    url(r'^download/$', views.downloadpage, name ='download'),
    url(r'^contact/$', views.contactpage, name ='contact'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.userlogin, name='login'),
    url(r'^logout/$', views.userlogout, name='logout'),
    url(r'^welcome/$', views.userpage, name ='welcome'),
    url(r'^download_app/musiana.tar.gz$',views.downloadapp,),
    url(r'^playlist/$', views.playlist, name='playlist'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
