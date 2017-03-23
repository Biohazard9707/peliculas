from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .forms import UserRegistrationForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.

class ProfileView(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name = "accounts/profile.html"
		user_profile = get_object_or_404(Profile, user_profile=request.user)
		context = {
			'usuario':user_profile,
		}
		return render(request, template_name, context)

class RegistryView(View):
	def get(self, request):
		template_name = "accounts/registration.html"
		form = UserRegistrationForm()
		form_user = ProfileForm()
		context = {
			'form':form,
			'form_user':form_user,
		}
		return render(request, template_name, context)

	def post(self, request):
		template_name = "accounts/registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		new_user_photo = ProfileForm(request.POST,request.FILES)
		if new_user_form.is_valid() and new_user_photo.is_valid():
			new_user = new_user_form.save(commit=False)
			new_photo = new_user_photo.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password2'])
			new_user.save()
			new_photo.user_profile = new_user
			new_photo.email = new_user.email
			new_photo.save()
			return redirect('accounts:profile')
		else: 
			context = {
				'form':new_user_form,
				'form_user':new_user_photo,
			}
			return render(request, template_name, context)
