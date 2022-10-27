from django.urls import path

from web.views import notes_view, main_view, note_view, note_edit_view, registration_view, login_view, logout_view

urlpatterns = [
    path("", main_view),
    path("", main_view, name='main'),
    path("registration/", registration_view, name='registration'),
    path("login/", login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path("notes/", notes_view, name="notes_list"),
    path("notes/add/", note_edit_view, name="notes_add"),
    path("notes/<int:id>/", note_view, name="note"),
    path("notes/<int:id>/edit/", note_edit_view, name="note_edit"),
]