from django.contrib import admin

from blog.models import Category, Tag, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'category', 'author')
    ordering = ('-created_time',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
