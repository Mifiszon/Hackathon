from django.db import models

class FeedInfo(models.Model):
    feed_publisher_name = models.CharField(max_length=255)
    feed_publisher_url = models.URLField()
    feed_lang = models.CharField(max_length=10)
    feed_start_date = models.DateField(blank=True, null=True)
    feed_end_date = models.DateField(blank=True, null=True)
