from django.urls import path, include
from .views import post, posts, info, index, error, access


post_route = [
    path('', post), #http://127.0.0.1:8000/route/posts/4
    path('info', info), #http://127.0.0.1:8000/route/posts/4/info?comments=0&likes=22
]

urlpatterns = [
    path('posts/<int:id>/', include(post_route)),
    path('posts', posts, name='posts'),
    path('index', index, name='index'),
    path('error', error, name='error'),
    path('access', access, name='access'),
]
