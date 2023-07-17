
from django.contrib import admin
from .models import Article, Tags, ArticleTagsPositions


class ArticleTagsPositionsInline(admin.TabularInline):
    model = ArticleTagsPositions
    extra = 3


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    list_filter = ['title']
    inlines = [ArticleTagsPositionsInline,]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
