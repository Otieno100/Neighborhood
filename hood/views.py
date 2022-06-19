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
    return render(request, 'hood/profile.html', {'profile': profile, 'posts': posts})    


   



def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'hood/search.html',{"message":message,"posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'awwards/search.html',{"message":message})



def single_neighbourhood(request):
    neighbourhood = Neighbourhood.objects.all()
   
    return render (request, 'hood/neighbourhood.html',{'neighbourhood':neighbourhood})
