from django.urls import path
from . import views

from .views import SearchResultsView
 

urlpatterns = [
	path('', views.home, name = 'home'),
	path('about', views.about, name = 'about'),
	path('artists', views.artists, name = 'artists'),
	path('artists/<artist_id>', views.artist, name = 'artist'),
	path('pictures', views.pictures, name = 'pictures'),
	path('pictures/<picture_id>', views.picture, name = 'picture'),
	path('search/', SearchResultsView.as_view(), name = 'search_results'),
]
