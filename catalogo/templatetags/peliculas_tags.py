from django import template
from django.db.models import Count

register = template.Library()

from ..models import Movie

@register.simple_tag
def total_movies():
	return Movie.objects.all().count()

@register.inclusion_tag('catalogo/ultimas_peliculas.html')
def show_movies(count=5):
	ultimates_movies = Movie.objects.all().order_by('-fecha')[:count]
	return {'ultimates_movies':ultimates_movies, }