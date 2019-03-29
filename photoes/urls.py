from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name ='welcome'),  
    url(r'^profile/', views.my_profile, name='profile'),
    url(r'^view_profile', views.view_profile, name='view_profile'),
    url(r'^upload_image', views.upload_image, name='upload_image'),
    url(r'^search', views.search_results, name='search'),
    url(r'^comment', views.display_commentForm, name='comment'),
    url(r'^view_comment', views.view_comment, name='view_comment'),
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)