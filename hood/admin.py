from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Neighbourhood, Business,Profile,Post

admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Post)
admin.site.register(Profile)