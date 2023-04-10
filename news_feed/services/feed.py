from news_feed.models import NewsFeed


class FeedService:
    @staticmethod
    def create_feed(user_id, feed_id, feed_text):
        # creating entry in model
        feed = NewsFeed.create_feed(
            user_id=user_id,
            feed_id=feed_id,
            feed_text=feed_text,
        )
        return feed

    @staticmethod
    def get_feed():
        feed = NewsFeed.get_feed()
        return feed
