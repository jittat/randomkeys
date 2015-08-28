from django.contrib import admin

from .models import Room, Keyword

admin.site.register(Room)

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('name', 'room')
    list_filter = ['room__title']
    search_fields = ['room__title']

admin.site.register(Keyword, KeywordAdmin)
