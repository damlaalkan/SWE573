from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Profile, Post 
from .forms import PostForm 

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def dashboard(request):
    form = PostForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid() :
            post = form.save(commit=False)
            post.user = request.user
            post.save()  



            return redirect("dashboard")
    followed_dweets = Post.objects.filter(user__profile__in=request.user.profile.follows.all()).order_by("-created_at")
    #form = PostForm()
    return render(request, "dashboard.html", {"form": form,"posts": followed_dweets } )


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "profile_list.html", {"profiles": profiles})

def profile(request, pk):
    #if not hasattr(request.user, 'profile'):
    #    missing_profile = Profile(user=request.user)
    #    missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "profile.html", {"profile": profile})