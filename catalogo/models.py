from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True, unique=True)
	description = models.TextField()

	class Meta:
		ordering=('name',)
		verbose_name='category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('catalogo:movie_list_category', args=[self.slug])


class Movie(models.Model):
	user_movie = models.ForeignKey(User, related_name="movie_user", blank=True, null=True)
	category = models.ManyToManyField(Category, related_name='category_movie')
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, db_index=True)
	image = models.ImageField(upload_to='movies/%Y/%m/%d', blank=True)
	description = models.TextField()
	runtime = models.CharField(max_length=15)
	year = models.CharField(max_length=4)
	formatt = models.CharField(max_length=15)
	# date = models.DateTimeField(auto_now_add=True)
	tags = TaggableManager()

	class Meta:
		ordering=('name',)
		index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('catalogo:detail_movie', args=[self.id, self.slug])


class Comment(models.Model):
	user_comment = models.ForeignKey(User, related_name="comment_user")
	movie_comment = models.ForeignKey(Movie, related_name="comment_movie")
	datee = models.DateTimeField(auto_now_add=True)
	body = models.CharField(max_length=500)

	class Meta:
		ordering=('datee',)

	def __str__(self):
		return self.user_comment.username
