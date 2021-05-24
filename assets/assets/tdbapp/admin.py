from django.contrib import admin
from .models import Leads, Post
# Register your models here.
models_lst = [Leads]
admin.site.register(models_lst)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)