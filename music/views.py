from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Album
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm


from django.conf import settings
from django.http import HttpResponse


class IndexView(generic.ListView):
	template_name = 'music/index.html'
	model = Album

	# the code bellow do the same as the line 8
	# def get_queryset(self):
		# return Album.objects.all() 

class DetailView(generic.DetailView):
	template_name = 'music/details.html'
	model = Album

class AlbumCreate(CreateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']


class AlbumUpdate(UpdateView):
	model = Album
	fields = ['artist', 'album_title', 'genre', 'album_logo']

class AlbumDelete(DeleteView):
	model = Album
	success_url = reverse_lazy('music:index')


class UserFormView(View):
	form_class = UserForm
	template_name = 'music/registration_form.html'

	# display blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit = False)

			# cleaned (normalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			# returns User objects if credentials are correct
			user = authenticate(username=username, password = password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('music:index')

		return render(request, self.template_name, {'form': form})







# def get_object(self):
# 	static_files = settings.STATICFILES_DIRS
# 	static_root = settings.STATIC_ROOT
# 	media_root = settings.MEDIA_ROOT
# 	media_url = settings.MEDIA_URL

# 	if media_url:
# 		path = media_url
# 	else:
# 		path ='No object'
		
# 	return HttpResponse(path)
	

