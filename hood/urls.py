from django.urls import re_path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    # re_path('^$',views.welcome,name = 'welcome')
    re_path(r'^$',views.single_neighbourhood,name='hood'),
    re_path(r'^search/', views.search_results, name='search_results'),
    re_path(r'^accounts/', include('registration.backends.simple.urls')),
    re_path(r'^new/article$', views.new_neighbourhood, name='new-neighbourhood'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)