from django.conf.urls import url
from genfier import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^upload/$', views.fileupload, name='upload'),
    url(r'^$', views.homepage, name ='home'),
    url(r'^about/$', views.aboutpage, name ='about'),
    url(r'^download/$', views.downloadpage, name ='download'),
    url(r'^contact/$', views.contactpage, name ='contact'),
    url(r'^welcome/$', views.userpage, name ='welcome'),
    url(r'^download_app/musiana.tar.gz$',views.downloadapp,),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
