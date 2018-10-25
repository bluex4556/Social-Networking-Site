from django.urls import path
from . import views


urlpatterns= [
    path('',views.index,name='index'),
    path(r'profile/', views.UserProfileView,name='profileview'),
    path('posts/', views.posthome,name= 'posthome'),
    path('posts/<int:posts_id>/', views.detail, name='detail'),
    path('blog/<int:blog_id>/',views.bloghome,name='bloghome'),
    path('blog/posts/<int:blogpost_id>/', views.blogposts, name='blogpost_detail'),
]
