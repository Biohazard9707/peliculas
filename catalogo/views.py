from django.shortcuts import render, get_object_or_404
from .models import Movie, Category
from django.views.generic import View

# Create your views here.
class ListMovie(View):
	def get(self, request, category_slug=None):
		template_name = "catalogo/list-movies.html"
		category = None
		categories = Category.objects.all()
		movies 	= Movie.objects.all()
		if category_slug:
			category = get_object_or_404(Category, slug=category_slug)
			movies = movies.filter(category = category)
		context = {
			'category':category,
			'movies':movies,
			'categories':categories,
			'category_slug': category_slug,
		}
		return render(request, template_name, context)

class DetailMovie(View):
	def get(self, request, id, slug):
		template_name = "catalogo/detail-movie.html"
		movie = get_object_or_404(Movie, id=id, slug=slug)
		context = {
			'movie':movie,
		}
		return render(request, template_name, context)