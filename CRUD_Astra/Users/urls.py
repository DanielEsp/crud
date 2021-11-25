from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path("", views.user, name="main_user"),
    path("add/", views.add, name="add_user"),
    path("delete/<int:user_id>/", views.delete, name="delete_user"),
    path("edit/<int:user_id>/", views.edit, name="edit_user"),
]