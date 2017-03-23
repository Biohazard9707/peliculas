from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
	user_profile = models.OneToOneField(settings.AUTH_USER_MODEL)
	photo = models.ImageField(upload_to='users', blank=True)
	tel = models.CharField(max_length = 10, blank = True, null = True)
	email = models.EmailField()
	# fecha = models.CharField(max_lenght=4)
	
	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user_profile.username)