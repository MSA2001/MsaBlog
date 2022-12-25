from django.contrib import admin
from .models import profile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.


class ProfileInline(admin.StackedInline):
    model = profile
    can_delete = False


class ExtendedUserAdmin(UserAdmin):
    inlines = (ProfileInline,)


admin.site.unregister(User)
admin.site.register(User, ExtendedUserAdmin)
