from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from volunteer.models import Volunteer

from .models import UserProfile
from .forms import UserForm, UserProfileForm


# Create your views here.

class HomeView(View):

	def get(self,request):
		object_list = Volunteer.objects.all().order_by("-average_rating")

		paginator = Paginator(object_list, 2) # Show 25 contacts per page
		page_request_var = "page"
		page = request.GET.get(page_request_var)
		try:
			object = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			object = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			object = paginator.page(paginator.num_pages)


		context = {
			"object_list": object,
			"page_request_var": page_request_var,
			"title":"List of Top Rated Manpowers",
		}

		return render(request, "home.html", context)

class MainView(View):

	def get(self, request):
		return render(request, 'main.html')

class ProfileView(	View):

	def get(self,request, slug=None):
		object = get_object_or_404(UserProfile, slug=slug)

		context = {
			"object":object,
			"title":"UserProfile"
		}

		return render (request, "user/profile.html", context)


class ListView(View):

	def get(self,request):
		object_list = UserProfile.objects.all() #.order_by("-timestamp")
		paginator = Paginator(object_list, 5) # Show 25 contacts per page
		page_request_var = "page"
		page = request.GET.get(page_request_var)
		try:
			object = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			object = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			object = paginator.page(paginator.num_pages)


		context = {
			"object_list": object,
			"page_request_var": page_request_var,
			"title":"UserList"
		}
		return render(request, "user/list.html", context)


class UpdateView(View):

	def get(self,request,slug=None):
		instance = get_object_or_404(UserProfile, slug=slug)
		user_form = UserForm(instance=instance.user)
		profile_form = UserProfileForm(instance=instance)

		context = {
			"instance":instance,
			"user_form":user_form,
			"profile_form":profile_form,
			"title":"Update Profile"
		}

		return render(request, "user/update.html", context)

	def post(self, request, slug=None):
		instance = get_object_or_404(UserProfile, slug=slug)
		user_form = UserForm(request.POST or None, instance=instance.user)
		profile_form = UserProfileForm(request.POST or None,request.FILES or None,instance=instance)
		if user_form.is_valid() and profile_form.is_valid():

			user_form.save()
			profile_form.save()
			return HttpResponseRedirect(instance.get_absolute_url())
		else:
			print(user_form.errors,profile_form.errors)

		context = {
			"instance":instance,
			"title":"Update Profile"

		}

		return render (request, "user/update.html", context)

#LoginRequiredMixin
class DeleteView(View):

	def get(self,request,slug):
		instance = get_object_or_404(UserProfile, slug=slug)
		user = instance.user
		instance.delete()
		user.delete()

		return redirect('home')

class BlockView(View):

	def get(self,request,slug):
		instance = get_object_or_404(UserProfile, slug=slug)
		instance.blocked = True
		instance.save()

		return redirect('home')
