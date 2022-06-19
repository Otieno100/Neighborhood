from django.http  import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .models import Post, Profile, Business, Neighbourhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def welcome(request):
    return HttpResponse('Neighborhood')


def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    posts = Post.objects.filter(user = user)
    return render(request, 'all-posts/profile.html', {'profile': profile, 'posts': posts})    


   
def search(request):
    if 'site' in request.GET and request.GET['site']:
        search_term = request.GET.get('site')
        businesses = Business.objects.filter(name__icontains = search_term)
        message = f'{search_term}'
        return render(request, 'all-posts/search.html', {'businesses': businesses, 'message': message})
        
    return render(request, 'all-posts/search.html')    