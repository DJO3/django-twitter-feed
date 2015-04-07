from django.db import models


class TweetManager(models.Manager):

    def get_latest_tweets(self, offset=0, limit=10):
        return self.all().order_by('-published_at')[offset:limit]

    def remove_all(self):
        self.all().delete()


class Tweet(models.Model):
    """
    Cached imported tweet
    """
    id_str = models.TextField(u"id_str", max_length=64)
    screen_name = models.TextField(u"screen_name", max_length=128)
    content = models.TextField(u"Tweet Content", max_length=20000)
    published_at = models.DateTimeField(u"Published At")
    updated_at = models.DateTimeField(u"Last Update", auto_now=True)
    created_at = models.DateTimeField(u"Date", auto_now_add=True)

    objects = TweetManager()

    class Meta:
        verbose_name = 'Tweet'
        verbose_name_plural = 'Tweets'

    def __str__(self):
        return self.content