from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="camera_index"),
    path("video_feed", views.video_feed, name="video_feed"),
]