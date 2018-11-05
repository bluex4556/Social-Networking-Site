from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import profile,userintrests,posts,blog,blogpost,blogtags,comunity,comunityintrest
# Register your models here.

class userintrestsInline(admin.StackedInline): #inline class for userintrests
    model=userintrests
# adds intrest field to profile in django admin
@admin.register(profile)
class profileAdmin(admin.ModelAdmin):
    inlines= [
        userintrestsInline,
    ]
#inline class for profile
class profileInline(admin.StackedInline):
    model=profile
    can_delete= False
    fk_name= 'user'

# Make profile editable in user in django admin
class CustomUserAdmin(UserAdmin):
    inlines=(profileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request,obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(userintrests)
class userintrestsAdmin(admin.ModelAdmin):
    pass

admin.site.register(posts)

class blogtagsInline(admin.StackedInline):
    model= blogtags
@admin.register(blog)

class blogAdmin(admin.ModelAdmin):
    inlines=[
        blogtagsInline,
    ]

admin.site.register(blogtags)
admin.site.register(blogpost)

class  comunityintrestInline(admin.StackedInline):
    model = comunityintrest

class comunityAdmin(admin.ModelAdmin):
     model= comunity
     filter_horizontal = ('users',)
     inlines = [ comunityintrestInline,
        ]

admin.site.register(comunity,comunityAdmin)
