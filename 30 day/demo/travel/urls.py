from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path("adduser", views.AddData, name="add_user"),
]