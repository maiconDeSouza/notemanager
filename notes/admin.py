from django.contrib import admin
from .models import Note

# Register your models here.


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'important')


# Register your models here
admin.site.register(Note, NoteAdmin)
