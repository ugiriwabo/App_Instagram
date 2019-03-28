from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name ='welcome'),  
    url(r'^profile/', views.my_profile, name='profile'),
    url(r'^view_profile', views.view_profile, name='view_profile'),
    url(r'^upload_image', views.upload_image, name='upload_image'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)