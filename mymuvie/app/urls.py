from django.urls import path

from . import views

app_name = "app"
urlpatterns = [
    path("", views.index, name="index"),
    path("search/", views.search, name="search"),
    path("save/", views.save, name="save"),
]