from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("display_list", views.ContactList.as_view(), name="display_list"),
    path("delete/<int:pk>", views.delete, name="delete"),
]
