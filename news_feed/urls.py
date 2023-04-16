from django.urls import path

from news_feed.views.news_feeds import news_feed
from news_feed.views.likes import likes

urlpatterns = [
    path("", news_feed),
    path("likes/", likes),
]
