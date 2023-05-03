from django.urls import path
from . import views

urlpatterns = [
    path("", views.about_page, name='about_page'),
    path("youtube/", views.youtube_page, name='youtube_page')
]