from django.http import HttpResponseRedirect

from news_feed.services.feed import FeedService


def likes(request):
    request_get = request.GET
    feed_id = request_get.get("feed_id")
    likes = FeedService.like_feed(feed_id)

    return HttpResponseRedirect("/feed/")
