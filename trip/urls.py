from django.urls import path
from .views import HomeView , TripsList , TripCreateView, TripDetailView,NoteDetailView,NoteListView,NoteCreateView,NoteDeleteView,NoteUpdateView,TripDeleteView,TripUpdateView

urlpatterns = [
    path("",HomeView.as_view(), name='home'),
    path("dashboard/",TripsList, name='trip-list'),
    path("dashboard/note/",NoteListView.as_view(), name='note-list'),
    path("dashboard/note/create/",NoteCreateView.as_view(), name='note-create'),# note_form.html
    path("dashboard/trip/create/",TripCreateView.as_view(), name='trip-create'),# trip_form.html
    path("dashboard/trip/<int:pk>/",TripDetailView.as_view(), name='trip-detail'),
    path("dashboard/trip/<int:pk>/update/",TripUpdateView.as_view(), name='trip-update'),
    path("dashboard/trip/<int:pk>/delete",TripDeleteView.as_view(), name='trip-delete'),
    path("dashboard/note/<int:pk>/",NoteDetailView.as_view(), name='note-detail'),
    path("dashboard/note/<int:pk>/update/",NoteUpdateView.as_view(), name='note-update'), # update - uses same template as the create note_form.html
    path("dashboard/note/<int:pk>/delete/",NoteDeleteView.as_view(), name='note-delete'), # delete does note need a template
]

# model_list.html

