from django.contrib import admin

# Register your models here.
from .models import japan_ver81

@admin.register(japan_ver81)
class UserAdmin(admin.ModelAdmin):
	pass
