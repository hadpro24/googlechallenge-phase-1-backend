from rest_framework import serializers
from django.contrib.auth.models import User

from .models import (
    Film, Actor, Genre, Writer,
    Director, Award, Language
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username']

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Actor
        fields = ['id','name']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Genre
        fields = ['id', 'name']

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Writer
        fields = ['id', 'name']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Director
        fields = ['id', 'name']

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Award
        fields = ['id', 'name', 'received_it']

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Language
        fields = ['id', 'name']

#film model
class FilmSerializer(serializers.ModelSerializer):
    genres    = GenreSerializer(many=True, read_only=True)
    directors = DirectorSerializer(many=True, read_only=True)
    writers   = WriterSerializer(many=True, read_only=True)
    actors    = ActorSerializer(many=True, read_only=True)
    awards    = AwardSerializer(many=True, read_only=True)
    languages = LanguageSerializer(many=True, read_only=True)

    class Meta:
        model = Film
        fields = ['id', 'title', 'released', 'genres', 'description', 'runtime',
         'directors', 'writers', 'actors', 'country','languages', 'awards', 'rated', 'image']
