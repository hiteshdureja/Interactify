from django.db import models
from account.models import Users
from common.models import BaseModel


class NewsFeed(BaseModel):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, max_length=255)
    feed_id = models.AutoField(primary_key=True)
    feed_text = models.TextField(null=False)

    class Meta:
        db_table = "news_feed"

    @staticmethod
    def create_feed(user_id, feed_text):
        feed = NewsFeed.objects.create(
            user_id=user_id,
            feed_text=feed_text,
        )
        return feed

    @staticmethod
    def get_feed():
        feed = NewsFeed.objects.all()
        return feed
