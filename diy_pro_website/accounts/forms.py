from django import forms
from django.contrib.auth.models import User
from .models import Profile


class ExpertSignupForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ["display_name", "contact_info", "bio", "tags"]
        widgets = {"tags": forms.CheckboxSelectMultiple}

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password and len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters long.")
        return password
