from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from social import views as socialview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/',include('social.urls')),
    path('accounts/',include('accounts.urls')),
    path('', socialview.posthome, name='home'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
