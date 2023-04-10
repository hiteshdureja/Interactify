from django.shortcuts import render

from news_feed.constants import NEWS_FEEDS
from news_feed.services.feed import FeedService


def news_feed(request):
    request_post = request.POST
    user_id = request_post.get("user_id")
    feed_text = request_post.get("feed_text")

    if not user_id or not feed_text:
        feed = FeedService.get_feed()
        return render(request, NEWS_FEEDS, {
            "feed": feed
        })

    FeedService.create_feed(
        user_id=user_id,
        feed_text=feed_text,
    )
    return render(request, NEWS_FEEDS, {})
