from django.urls import path

from news_feed.views.news_feeds import news_feed

urlpatterns = [
    path("", news_feed),
]
