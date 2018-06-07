from django.urls import path

from youtubewatch.views import VideoList

urlpatterns = [
    path('index/', VideoList.as_view()),
]
