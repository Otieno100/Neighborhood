from django.urls import include, re_path
# from django.conf.urls import include, re_path


from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path(r'',include('hood.urls')),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    re_path(r'^logout/', auth_views.logout_then_login),
  
]

