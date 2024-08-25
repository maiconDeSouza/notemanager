from django.contrib import admin
from django.urls import path
from notes.views import NotesList, CreateNote, DetailNote, DeleteNote, UpdateNote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NotesList.as_view(), name="note_list"),
    path('create', CreateNote.as_view(), name='create_note'),
    path('detail/<str:pk>', DetailNote.as_view(), name='details_note'),
    path('delete/<str:pk>', DeleteNote.as_view(), name='delete_note'),
    path('update/<str:pk>', UpdateNote.as_view(), name='update_note')
]
