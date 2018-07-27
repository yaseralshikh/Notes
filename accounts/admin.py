from django.contrib import admin

# Register your models here.

from .models import ProFile

class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['headline', 'join_data']
    list_display = ['user', 'slug', 'headline', 'join_data']
    search_fields = ['user__username','user__first_name' , 'headline' , 'bio']



admin.site.register(ProFile, ProfileAdmin)
