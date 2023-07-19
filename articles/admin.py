
from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tags, ArticleTagsPositions


class PositionsInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_ismain = 0
        for form in self.forms:
            if form.cleaned_data.get('is_main', False):
                count_ismain += 1
            if count_ismain > 1:
                raise ValidationError('Основной тег может быть только один')

        if count_ismain == 0:
            raise ValidationError('Укажите основной тег')

        return super().clean()


class ArticleTagsPositionsInline(admin.TabularInline):
    model = ArticleTagsPositions
    extra = 3
    formset = PositionsInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at']
    list_filter = ['title']
    inlines = [ArticleTagsPositionsInline,]


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
