from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page="/accounts/login/"),
        name="logout",
    ),
    path("delete_account/", views.delete_account, name="delete_account"),
]
