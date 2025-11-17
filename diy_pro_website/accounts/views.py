from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import ExpertSignupForm, EditProfileForm
from .models import Tag, Profile


def signup(request):
    form = ExpertSignupForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Create the user
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            profile = form.save(commit=False)
            profile.user = user
            profile.save()
            form.save_m2m()
            login(request, user)
            return redirect("profile", user_id=user.id)
        else:
            # Print errors to console for debugging
            print("Form errors:", form.errors)

    tags = Tag.objects.all()
    return render(request, "signup.html", {"form": form, "tags": tags})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("profile", user_id=request.user.id)

    error = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("profile", user_id=user.id)
        else:
            error = "Invalid credentials"
    return render(request, "login.html", {"error": error})


@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile", user_id=request.user.id)
        else:
            print("Form errors:", form.errors)
    else:
        form = EditProfileForm(instance=profile)

    tags = Tag.objects.all()
    return render(request, "edit_profile.html", {"form": form, "tags": tags})


def profile(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    return render(request, "profile.html", {"profile": profile})
