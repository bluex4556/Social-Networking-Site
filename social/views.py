from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import profile,posts,blog,blogpost,userintrests,blogtags,Friend
from django.http import Http404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return HttpResponse("Hello")


def UserProfileView(request):
    username = None
    if request.user.is_authenticated:
        temp = request.user
        profiles= profile.objects.get(user= temp)
        intrestlist = userintrests.objects.filter(Profile = profiles).values('intrest')

        try:
            friends = Friend.objects.get(current_user= temp)
            friendslist = friends.users.all()
        except Friend.DoesNotExist:
            friendslist = False

        context = {'profile': profiles,
            'intrestlist': intrestlist,
            'friendslist':friendslist,}
        return render(request, 'social/profile.html', context)
    else:
        return HttpResponse("fail")

def posthome(request):
    latest_posts_list = posts.objects.order_by('-pub_date')[:5]
    context= {'latest_posts_list':latest_posts_list}
    return render(request, 'social/posthome.html', context)

def detail(request, posts_id):
    post = get_object_or_404(posts, pk=posts_id)
    return render(request, 'social/detail.html', {'post': post})

def bloghome(request, blog_id):
    blogs= blog.objects.get(pk=blog_id)
    taglist= blogtags.objects.filter( blog = blogs ).values('tags')
    latest_posts_list = blogpost.objects.order_by('-pub_date')[:5]
    context= {'latest_posts_list':latest_posts_list,
              'blogs': blogs,
              'taglist':taglist,}
    return render(request, 'social/bloghome.html', context)
def blogposts(request,blogpost_id):
    posts= blogpost.objects.get(pk=blogpost_id)
    return render(request, 'social/blogdetail.html', {'posts': posts})

def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('index')
