from django.contrib import admin

from .models import Film, Actor, Director, Writer, Genre, Language, Award
# Register your models here.
admin.site.register(Film)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Writer)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Award)
