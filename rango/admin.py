from contextlib import nullcontext
from rango.models import Category, Page,UserProfile
# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import User
from rango.models import UserProfile

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class PageAdmin(admin.ModelAdmin):
    list_display = ['title','category','url']
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)
admin.site.register(UserProfile)