from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .forms import ExpertSignupForm, EditProfileForm
from .models import Tag, Profile
from django.db.models import Count, Q


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
        try:
            User.objects.get(id=request.user.id)
            # User exists, send to profile
            return redirect("profile", user_id=request.user.id)
        except User.DoesNotExist:
            logout(request)
            return redirect("login")

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


@login_required
def delete_account(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect("login")


def profile(request, user_id):
    profile = Profile.objects.get(user__id=user_id)
    return render(request, "profile.html", {"profile": profile})


def search_users(request):
    query = request.GET.get("q", "")
    tag_ids = request.GET.getlist("tags")  # list of selected tag IDs as strings

    profiles = Profile.objects.all()

    # Name search
    if query:
        profiles = profiles.filter(
            Q(user__username__icontains=query) | Q(display_name__icontains=query)
        )

    # Require all selected tags
    if tag_ids:
        # convert to ints
        tag_ids_int = list(map(int, tag_ids))
        profiles = (
            profiles.filter(tags__in=tag_ids_int)
            .annotate(num_tags=Count("tags"))
            .filter(num_tags__gte=len(tag_ids_int))
        )

    tags = Tag.objects.all()

    return render(
        request,
        "search_users.html",
        {
            "profiles": profiles,
            "tags": tags,
            "query": query,
            "selected_tags": list(map(str, tag_ids)),  # keep as strings for template
        },
    )
