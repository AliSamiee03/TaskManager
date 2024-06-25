from django.contrib import admin
from .models import UserAccount

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAccount, UserAccountAdmin)