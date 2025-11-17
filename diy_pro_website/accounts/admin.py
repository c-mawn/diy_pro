from django.contrib import admin
from .models import Profile, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("display_name", "user")
    list_filter = ("tags",)
    search_fields = ("display_name", "user__username")
