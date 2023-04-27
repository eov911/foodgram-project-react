from django.contrib import admin

from .models import Favourite, Ingredient, Recipe, Shopping, Tag


class IngredientsRecipeLine(admin.TabularInline):
    """ Связь  ингридиентов в рецепте """
    model = Recipe.ingredients.through


class IngredientAdmin(admin.ModelAdmin):
    """ Панельь управление ингридиентами """
    list_display = ('name', 'measurement_unit')
    search_fields = ('name', )
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class TagAdmin(admin.ModelAdmin):
    """ Панель управление тегами """
    list_display = ('name', 'color', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name', )
    empty_value_display = '-пусто-'


class RecipeAdmin(admin.ModelAdmin):
    """ Панель управление рецептами """
    list_display = ('name', 'author', 'favorites')
    search_fields = ('author', 'name')
    list_filter = ('tags', )
    filter_horizontal = ('tags', )
    empty_value_display = '-пусто-'
    inlines = (IngredientsRecipeLine,)

    def favourites(self, obj):
        if Favourite.objects.filter(recipe=obj).exists():
            return Favourite.objects.filter(recipe=obj).count()
        return 0

    favourites.short_description = 'Количество добавлений рецепта в избранное'


class FavoriteAdmin(admin.ModelAdmin):
    """ Панель управление подписками """
    list_display = ('user', 'recipe')
    list_filter = ('user', 'recipe')
    search_fields = ('user', 'recipe')
    empty_value_display = '-пусто-'


class ShoppingCartAdmin(admin.ModelAdmin):
    """ Панель список покупок """
    list_display = ('recipe', 'user')
    list_filter = ('recipe', 'user')
    search_fields = ('user', )
    empty_value_display = '-пусто-'


admin.site.register(Ingredient)
admin.site.register(Tag)
admin.site.register(Favourite)
admin.site.register(Recipe)
admin.site.register(Shopping)