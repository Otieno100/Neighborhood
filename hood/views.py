from django.http  import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login
from .models import Post, Profile, Business, Neighbourhood
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required

from .forms import NewNeighbourhoodForm
from django.http  import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
def welcome(request):
    return HttpResponse('Neighborhood')


def profile(request, username):
    user = User.objects.get(username = username)
    profile = Profile.objects.get(user = user)
    posts = Post.objects.filter(user = user)
    return render(request, 'hood/profile.html', {'profile': profile, 'posts': posts})    


   



def search_results(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbourhoods = Post.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'hood/search.html',{"message":message,"posts": searched_neighbourhoods})

    else:
        message = "You haven't searched for any term"
        return render(request, 'hood/search.html',{"message":message})


@login_required(login_url='/accounts/login/')
def single_neighbourhood(request):
    neighbourhood = Neighbourhood.objects.all()
   
    return render (request, 'hood/neighbourhood.html',{'neighbourhood':neighbourhood})


def business(request):
    business = Business.objects.all()
    return render(request, 'hood/business.html', {'business': business})



#.....
@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood = current_user
            neighbourhood.save()
        return redirect('hood')

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})    


@login_required(login_url='/accounts/login/')
def signUp(request,post_id):
    try:
        post = Post.objects.get(id = post_id)
    except ObjectDoesNotExist:
        raise Http404()
    return render(request,"registration/registration_form.html", {"post":post})

#    


@login_required
def join_hood(request, neighborhood_id):
    neighborhood = get_object_or_404(Neighbourhood, id=neighborhood_id)
    request.user.profile.neighbourhood = neighborhood
    request.user.profile.save()
    return redirect('hood', neighborhood_id = neighborhood.id)


# def join_hood(request,id):
#     neighbourhood = get_object_or_404(Neighbourhood,id=id)
#     request.user.profile.neighbourhood=neighbourhood
#     request.user.profile.save()
#     return redirect('home')

# def leave_hood(request,id):
#     hood = get_object_or_404(Neighbourhood,id=id)
#     request.user.profile.neighbourhood=None
#     request.user.profile.save()
#     return redirect('home')



