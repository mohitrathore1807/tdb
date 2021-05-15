from django.contrib import admin
from .models import Leads, Post
# Register your models here.
models_lst = [Leads, Post]
admin.site.register(models_lst)
