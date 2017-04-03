from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Category, Comment
from django.views.generic import View
from .forms import MovieForm, EmailPostForm, CommentForm

from taggit.models import Tag
from django.core.mail import send_mail

# Create your views here.
class ListMovie(View):
	def get(self, request, category_slug=None, tag_slug=None):
		template_name = "catalogo/list-movies.html"
		category = None
		tag = None
		categories = Category.objects.all()
		movies 	= Movie.objects.all()
		if category_slug:
			category = get_object_or_404(Category, slug=category_slug)
			movies = movies.filter(category = category)
		if tag_slug:
			tag = get_object_or_404(Tag, slug=tag_slug)
			movies = movies.filter(tags__in=[tag])
		context = {
			'category':category,
			'movies':movies,
			'categories':categories,
			'category_slug': category_slug,
			'tag':tag,
		}
		return render(request, template_name, context)

class DetailMovie(View):
	def get(self, request, id, slug):
		# form = EmailPostForm()
		form = CommentForm()
		template_name = "catalogo/detail-movie.html"
		movie = get_object_or_404(Movie, id=id, slug=slug)
		comments = movie.comment_movie.all()
		# comments = Comment.objects.all().filter(movie_comment = movie)
		context = {
			# 'form':form,
			'form':form,
			'movie':movie,
			'comments':comments,
		}
		return render(request, template_name, context)

	def post(self, request, id, slug):
		template_name = "catalogo/detail-movie.html"
		movie = get_object_or_404(Movie, id=id, slug=slug)
		comments = movie.comment_movie.all()
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save(commit=False)
			new_comment.user_comment = request.user
			new_comment.movie_comment = movie
			new_comment.save()
			return redirect('catalogo:detail_movie', movie.id, movie.slug)
		else:
			form = CommentForm()
		# form = EmailPostForm(request.POST)
		# if form.is_valid():
		# 	cd = form.cleaned_data
		# 	movie_url = request.build_absolute_uri(movie.get_absolute_url())
		# 	subject = '{}, ({}) te recomienda esta pelicula "{}"'.format(cd['nombre'], cd['correo'], movie.name)
		# 	message = 'Ver pelicula {} de {}\n\n comentarios de {}: {} '.format(movie.name, movie_url, cd['nombre'], cd['comentarios'])
		# 	send_mail(subject, message, 'admin@mi_blog.com', [cd['para']])
		# 	return redirect('catalogo:list-movies') 
		# else:
		# 	form = EmailPostForm()
		context = {
			# 'form':form,
			'form':form,
			'movie':movie,
			'comments':comments,
		}
		return render(request, template_name, context)


class RegistryMovie(View):
	def get(self, request):
		template_name = "catalogo/registry-movie.html"
		form = MovieForm()
		context = {
			'form':form,
		}
		return render(request, template_name, context)

	def post(self, request):
		template_name = "catalogo/registry-movie.html"
		new_movie_form = MovieForm(request.POST, request.FILES)
		movie_form = MovieForm()
		if new_movie_form.is_valid():
			new_movie = new_movie_form.save(commit=False)
			new_movie.user_movie = request.user
			# category = Category.objects.all.filter()
			# print(new_movie.category)
			new_movie.save()
			return redirect('catalogo:list-movies')
		else: 
			context = {
				'form':movie_form,
			}
			return render(request, template_name, context)