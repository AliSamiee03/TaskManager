from django.contrib import admin
from .models import UserAccount, Tasks, Category, Comment

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserAccount, UserAccountAdmin)
admin.site.register([Tasks, Category, Comment])