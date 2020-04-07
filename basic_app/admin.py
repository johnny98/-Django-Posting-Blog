from django.contrib import admin
from .models import Post

#to register model in admin page
admin.site.register(Post)