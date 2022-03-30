from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Artist, Picture

# Create your views here.
def home(request):
	return render(request, 'pictures_home/home.html')


def about(request):
	return render(request, 'pictures_home/about.html')


def artists(request):

	artists = Artist.objects.order_by('name')

	context = {'artists': artists}
	return render(request, 'pictures_home/artists.html', context)




def artist(request, artist_id):

	artist = Artist.objects.get(id = artist_id)

	pictures = artist.picture_set.all()

	context = {'artist': artist, 'pictures':pictures}

	return render(request, 'pictures_home/artist.html', context)



def pictures(request):

	pictures = Picture.objects.order_by('name')

	context = {'pictures': pictures}
	return render(request, 'pictures_home/pictures.html', context)



def picture(request, picture_id):

	

	picture = Picture.objects.get(id = picture_id)

	artist = picture.artist_id

	context = {'picture': picture, 'artist': artist}

	return render(request, 'pictures_home/picture.html', context)




class SearchResultsView(ListView):


	#model = Picture
	template_name = 'pictures_home/search_results.html'

	def get_queryset(self):
		query = self.request.GET.get('q')
		object_list = Picture.objects.filter(
			Q(name__icontains=query) | Q(style__icontains = query) | Q(artist__name__icontains = query)
		)

		return object_list


