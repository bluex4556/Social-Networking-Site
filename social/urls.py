from django.urls import path
from . import views

app_name = 'social'

urlpatterns= [
    path('',views.index,name='index'),

    path('create/post', views.post_create, name= 'createpost'),
    path('create/<int:posts_id>/comment', views.comment_create, name= 'comment_create'),
    path(r'create/<int:blog_id>/blogpost/', views.blogpost_create, name= 'blogpost_create'),
    path('create/blog/',views.blog_create, name= 'blog_create'),
    path('create/<int:blog_id>/tags/', views.blogtags_create, name= 'blogtags_create'),

    path(r'profile/me', views.UserProfileView,name='profileview'),
    path(r'profile/<int:user_id>', views.OtherUserProfileView,name='profileview'),
    path('profile/me/update', views.ProfileUpdateView.as_view(), name='ProfileUpdate'),
    path(r'connect/<str:operation>/<int:pk>/', views.change_friends, name='change_friends'), #operation= add or remove

    path('posts/', views.posthome,name= 'posthome'),
    path('posts/<int:posts_id>/', views.detail, name='detail'),

    path('blog/<int:blog_id>/',views.bloghome,name='bloghome'),
    path('blog/posts/<int:blogpost_id>/', views.blogposts, name='blogpost_detail'),

    path('comunity/<int:comunity_id>',views.comunityhome, name = 'comunityhome'),
    path('related/', views.related, name= 'related'),
    path('blog/', views.BlogListView.as_view(), name = 'BlogListView'),

]
