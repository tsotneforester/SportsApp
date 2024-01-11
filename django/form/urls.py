from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("details/<str:entry>", views.task, name="task"),
    path("edit/<str:entry>", views.edit, name="edit"),
    path("delete", views.delete, name="delete"),
    path("update", views.update, name="update"),
    path("error", views.error, name="error"),
 
]