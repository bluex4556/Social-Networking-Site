from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import profile,posts,blog,blogpost,userintrests,blogtags,Friend,comunityintrest,comunity,comments
from django.http import Http404
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def index(request):
    return HttpResponse("Hello")

@login_required(login_url = '/accounts/login/')
def UserProfileView(request):
    username = None
    temp = request.user
    profiles= profile.objects.get(user= temp)
    intrestlist = userintrests.objects.filter(Profile = profiles).values('intrest')
    try:
        friends = Friend.objects.get(current_user= temp)
        friendslist = friends.users.all()
    except Friend.DoesNotExist:
        friendslist = False
    context = {
            'profile': profiles,
            'intrestlist': intrestlist,
            'friendslist':friendslist,
                }
    return render(request, 'social/profile.html', context)

def OtherUserProfileView(request, user_id):
    temp = get_object_or_404(User,pk=user_id)
    profiles= profile.objects.get(user= temp)
    intrestlist = userintrests.objects.filter(Profile = profiles).values('intrest')
    try:
        friends = Friend.objects.get(current_user= temp)
        friendslist = friends.users.all()
    except Friend.DoesNotExist:
        friendslist = False
    context = {
            'profile': profiles,
            'intrestlist': intrestlist,
            'friendslist':friendslist,
                }
    return render(request, 'social/profile.html', context)

def posthome(request):
    latest_posts_list = posts.objects.order_by('-pub_date')[:5]
    context= {'latest_posts_list':latest_posts_list}
    return render(request, 'social/posthome.html', context)

def detail(request, posts_id):
    post = get_object_or_404(posts, pk=posts_id)
    commentlist = comments.objects.filter(posts = post)
    context = {
            'post': post,
            'commentlist': commentlist,
            }
    return render(request, 'social/detail.html',context)

def bloghome(request, blog_id):
    blogs= blog.objects.get(pk=blog_id)
    taglist= blogtags.objects.filter( blog = blogs ).values('tags')
    latest_posts_list = blogpost.objects.filter(blog = blogs).order_by('-pub_date')[:5]
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

def comunityhome(request, comunity_id):
    comunity_= comunity.objects.get(pk=comunity_id)
    intrestlist= comunityintrest.objects.filter( comunity = comunity_ ).values('intrest')
    context= {'comunity': comunity_,
              'intrestlist':intrestlist,}
    return render(request, 'social/comunityhome.html', context)

@login_required(login_url = '/accounts/login/')
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            #save article to db
            return redirect('social:posthome')
    else:
        form = forms.CreatePost()
    return render(request, 'social/post_create.html', {'form':form})

@login_required(login_url = '/accounts/login/')
def blogpost_create(request,blog_id):
    if request.method == 'POST':
        form = forms.CreateBlogpost(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.blog = get_object_or_404(blog,id=blog_id)
            instance.save()
            #save article to db
            return redirect('social:posthome')
    else:
        form = forms.CreateBlogpost()
    return render(request, 'social/blogpost_create.html', {'form':form, 'blog_id':blog_id})

@login_required(login_url = '/accounts/login/')
def blog_create(request):
    if request.method == 'POST':
        form = forms.CreateBlog(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.user = request.user
            instance.save()
            return redirect('social:bloghome', blog_id= blog_id)
    else:
        form = forms.CreateBlog()
    return render(request, 'social/blog_create.html', {'form':form})

@login_required(login_url = '/accounts/login/')
def blogtags_create(request,blog_id):
    if request.method == 'POST':
        form = forms.CreateBlogtags(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.blog = get_object_or_404(blog, id=blog_id)
            instance.save()
            #save article to db
            return redirect('social:bloghome', blog_id= blog_id)
    else:
        form = forms.CreateBlogtags()
    return render(request, 'social/blogtags_create.html', {'form':form, 'blog_id':blog_id})

@login_required(login_url = '/accounts/login/')
def comment_create(request,posts_id):
    if request.method == 'POST':
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.posts = get_object_or_404(posts, id=posts_id)
            instance.user = request.user
            instance.save()
            #save article to db
            return redirect('social:detail',posts_id= posts_id)
    else:
        form = forms.CreateComment()
    return render(request, 'social/comment_create.html', {'form':form, 'posts_id':posts_id})

@login_required(login_url = '/accounts/login/')
def related(request):
    temp = request.user
    user_intrests = userintrests.objects.filter(Profile = temp.profile).values_list('intrest')
    user_intrest=  []
    for intrest in user_intrests:
        user_intrest.append(intrest[0])
    blogs =[]
    for intrest in user_intrest:
        try:
            tags =  blogtags.objects.get(tags = intrest)
            blogs.append(get_object_or_404(blog, id= tags.blog.id))
        except blogtags.DoesNotExist:
            pass
    context = {'blogs': blogs}
    return render(request, 'social/related.html', context)
