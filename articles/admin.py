from django.contrib import admin

from . import models
from .models import Author, Article, SubArticle, Comment, Tag, Category


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'bio')
    search_fields = ('name', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class SubArticleInlineAdmin(admin.TabularInline):
    model = SubArticle
    extra = 0


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'image', 'message', 'created_at')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = (SubArticleInlineAdmin, )
    list_display = ('id','title', 'get_author_name', 'created_date')
    search_fields = ('title', )

    def get_author_name(self, obj):
        return obj.author.name if obj.author else None

    get_author_name.short_description = 'Author Name'
