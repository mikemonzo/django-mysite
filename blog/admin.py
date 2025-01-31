from django.contrib import admin

from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish_at', 'status')
    list_filter = ('status', 'created_at', 'publish_at')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish_at'
    ordering = ('status', 'publish_at')
