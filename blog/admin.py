from django.contrib import admin
from .models import Post, Comment, Like, Story

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_at', 'total_likes']
    search_fields = ['title', 'author__username']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'created_at']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['post', 'user']

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['author', 'created_at']
