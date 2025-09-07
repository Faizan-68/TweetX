from django.contrib import admin
from .models import Tweet, Like,Comment



class TweetAdmin(admin.ModelAdmin):
    list_display = ('user','text','total_likes','updated_at','created_at')
    search_fields = ('text','user__username')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','comment','tweet','created_at')

# Register your models here.
admin.site.register(Tweet,TweetAdmin)
admin.site.register(Like)
admin.site.register(Comment, CommentAdmin)