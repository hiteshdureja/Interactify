import requests
from django.shortcuts import render

from news_feed.constants import NEWS_FEEDS
from news_feed.services.feed import FeedService

from django.http import HttpResponseRedirect


def news_feed(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return HttpResponseRedirect("/")

    request_post = request.POST
    feed_text = request_post.get("feed_text")

    if not user_id or not feed_text:
        feed = FeedService.get_feed()
        feed=feed[::-1]
        return render(request, NEWS_FEEDS, {"feed": feed})

    FeedService.create_feed(
        user_id=user_id,
        feed_text=feed_text,
    )
    feed = FeedService.get_feed()
    feed = feed[::-1]
    return render(request, NEWS_FEEDS, {
        "feed": feed,
        "user_id": user_id
        })

