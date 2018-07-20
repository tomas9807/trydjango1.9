from django.contrib import admin
from . import models
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp','updated']
    list_display_links = ['updated']
    list_filter = ['updated']
    list_editable = ['title']
    search_fields = ['title','content']

admin.site.register(models.Post,PostAdmin)
