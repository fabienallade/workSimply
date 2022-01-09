from django.contrib import admin

# Register your models here.
from .models import Post
from .forms import PostForm


class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'content', 'image']
    form = PostForm

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
