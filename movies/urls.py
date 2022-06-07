from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('details/<int:movie_id>', views.description, name='movies'),
]
