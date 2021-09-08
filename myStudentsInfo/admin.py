from django.contrib import admin

# Register your models here.
from .models import *
# admin.site.register(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('S_id','name','age','sex','father_name','mother_name','last_education')
