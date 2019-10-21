from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

#my model
from .models import (
    Actor, Writer, Director, Language, Award, Genre, Film
)
from .serializers import (
    FilmSerializer
)
# Create your views here.
class ListFilm(APIView):
    """
        list returns all film
    """
    def get(self, request):
        """
            get film
        """
        title_search   = request.query_params.get('search')
        films = Film.objects.all()
        if title_search:
            films = films.filter(title__contains=title_search)
            if not films.exists():
                return Response({'not_found': 'Not found.'})
        serializer  = FilmSerializer(films, many=True)
        return Response(serializer.data)

class GetFilm(APIView):
    """
        get a film
    """
    def get(self, request, pk):
        """
            film
        """
        film = get_object_or_404(Film, pk=pk)
        serializer = FilmSerializer(film)
        return Response(serializer.data)

class GetFavoritesFilm(APIView):
    """
        get films favorites
    """
    def get(self, request):
        films_favorite = request.query_params.get('ids')
        if not films_favorite:
            return Response({'not_found': 'Not found.'})
        ids = tuple(int(i) for i in films_favorite.split(','))
        films = Film.objects.filter(pk__in=(ids))
        if not films.exists():
            return Response({'not_found': 'Not found.'})
        serializer  = FilmSerializer(films, many=True)
        return Response(serializer.data)
