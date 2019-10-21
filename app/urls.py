from django.urls import path
from .views import (
    ListFilm, GetFilm, GetFavoritesFilm
)

urlpatterns = [
    path('films', ListFilm.as_view()),
    path('films/favorites', GetFavoritesFilm.as_view()),
    path('films/<int:pk>', GetFilm.as_view()),
]
