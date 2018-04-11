from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'created_time', 'text', 'post']

admin.site.register(Comment, CommentAdmin)
