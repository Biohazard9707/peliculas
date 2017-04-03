from django import forms 
# from django.contrib.auth.models import User
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ('name', 'slug', 'image', 'description', 'runtime', 'year', 'formatt',
			'category',)

class EmailPostForm(forms.Form):
	nombre = forms.CharField(max_length=25)
	correo = forms.EmailField()
	para = forms.EmailField()
	comentarios = forms.CharField(widget=forms.Textarea())

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('body',)