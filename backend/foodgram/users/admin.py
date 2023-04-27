from django.contrib import admin
from .models import User, Follow


class PostAdmin(admin.ModelAdmin):
    """ Панель управление пользователями """
    list_display = ('username', 'email', 'first_name', 'last_name')
    search_fields = ('email', 'username')
    list_filter = ('email', 'username')
    ordering = ('username', )
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    """ Панель управления подписками """
    list_display = ('user', 'author')
    list_display_links = ('user', )
    search_fields = ('user', )
    empty_value_display = '-пусто-'


admin.site.register(User)
admin.site.register(Follow)
