from django.urls import path

from news_feed.views import news_feed

urlpatterns = [
    path("", news_feed),
]
