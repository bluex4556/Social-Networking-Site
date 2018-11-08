from django.urls import path
from . import views

app_name = 'social'

urlpatterns= [
    path('',views.index,name='index'),
    path('create/post', views.post_create, name= 'createpost'),
    path(r'create/<int:blog_id>/blogpost/', views.blogpost_create, name= 'blogpost_create'),
    path(r'profile/', views.UserProfileView,name='profileview'),
    path(r'connect/<str:operation>/<int:pk>/', views.change_friends, name='change_friends'), #operation= add or remove
    path('posts/', views.posthome,name= 'posthome'),
    path('posts/<int:posts_id>/', views.detail, name='detail'),
    path('blog/<int:blog_id>/',views.bloghome,name='bloghome'),
    path('blog/posts/<int:blogpost_id>/', views.blogposts, name='blogpost_detail'),
    path('comunity/<int:comunity_id>',views.comunityhome, name = 'comunityhome'),

]
