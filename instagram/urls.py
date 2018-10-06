from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    url('^$', views.all_images, name ='allimages'),
    url(r'^search/', views.search_profile, name='search_profile'),
    url(r'^profile/(\d+)', views.my_profile, name='Profile'),
    url(r'^new/image$', views.new_post, name = 'new_post')

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
