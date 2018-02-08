from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[   
    url(r'^$',views.timelines, name='myGram'),
    url(r'^accounts/profile/', views.profile, name ='myProfile'),
    url(r'^new/status/(?P<username>[-_\w.]+)$', views.new_status, name='newStatus'),
    url(r'^user/(\d+)', views.user_profile, name='userProfiles'),
    url(r'^image/(\d+)', views.single_image, name='singleImage'),
    url(r'^profile/', views.find_profile, name='findProfile'),
    url(r'^single_image/likes/(\d+)', views.single_image_like, name='singleImageLike'),
    url(r'^new/comment/(?P<username>[-_\w.]+)$', views.new_comment, name='newComment'),
    url(r'^post/', views.post, name='post'),
]