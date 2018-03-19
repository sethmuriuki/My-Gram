from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[   
    url(r'^$',views.timelines, name='myGram'),
    url(r'^accounts/profile/', views.profile, name ='myProfile'),
    url(r'^new/status/(?P<username>[-_\w.]+)$', views.new_status, name='newStatus'),
    url(r'^image/(\d+)', views.single_image, name='singleImage'),
    url(r'^profile/', views.find_profile, name='findProfile'),
    url(r'^single_image/likes/(\d+)', views.single_image_like, name='singleImageLike'),
    url(r'^comment/(?P<username>[-_\w.]+)$', views.new_comment, name='newComment'),
    url(r'^post/', views.post, name='post'),
    url(r'profile/$',views.view_profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', views.view_profile, name='view_profile_with_pk'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)