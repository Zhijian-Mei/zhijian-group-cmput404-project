from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *

# Define an inline admin descriptor for Author model
# which acts a bit like a singleton
# refers to https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
class AuthorInline(admin.StackedInline):
    model = AuthorModel
    can_delete = False
    verbose_name_plural = 'author'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (AuthorInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)