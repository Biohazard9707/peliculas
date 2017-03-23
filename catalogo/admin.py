from django.contrib import admin
from .models import Category, Movie
# Register your models here.
# 
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug':('name',),}

class MovieAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'year', 'formatt']
	prepopulated_fields = {'slug':('name',),}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Movie, MovieAdmin)