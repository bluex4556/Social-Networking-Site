from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Create your models here.
class profile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE)
    dob=  models.DateField('date of birth',blank=True,null=True)
    avatar= models.ImageField(blank=True,null=True)
    address = models.CharField(max_length= 50, blank=True,null=True)
    work = models.CharField(max_length= 20, blank=True,null=True)
    education = models.CharField(max_length= 20, blank=True,null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save,sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile.objects.create(user=instance)
        instance.profile.save()
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

class userintrests(models.Model):
    Profile= models.ForeignKey(profile, related_name='intrests', on_delete= models.CASCADE)
    intrest = models.CharField(max_length=10)
    def __str__(self):
        return self.Profile.user.username +": "+ self.intrest

class Friend(models.Model):
    users = models.ManyToManyField(User)
    current_user = models.ForeignKey(User, related_name='owner', null=True, on_delete=models.CASCADE)

    @classmethod
    def make_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)

class posts(models.Model):
    user= models.ForeignKey(User,related_name='post_user',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField( null=True)
    pub_date = models.DateTimeField('Date published',default=timezone.now)
    rating = models.IntegerField('rating', default=0)
    def __str__(self):
        return self.title


    def __str__(self):
        return self.title
class blog(models.Model):
    user= models.ForeignKey(User,related_name='blog_user',on_delete=models.CASCADE)
    blogname= models.CharField(max_length=50)
    about= models.TextField(null=True)
    def __str__(self):
        return self.blogname

class blogtags(models.Model):
    blog= models.ForeignKey(blog,related_name='blog',on_delete=models.CASCADE)
    tags= models.CharField(max_length=10)
    def __str__(self):
        return self.blog.blogname+ ' ' + self.tags

class blogpost(models.Model):
    blog= models.ForeignKey(blog,related_name='blog_post',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(null=True)
    pub_date = models.DateTimeField('Date published',default=timezone.now)
    def __str__(self):
        return self.title
