import datetime

from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(null=True)  # If there is no modification, published date will be shown
    published_date = models.DateTimeField(blank=True, null=True)
    comment_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.published_date <= now

    def get_comment_count(self):
        return self.comment_count

    def new_comment(self):
        self.comment_count += 1
        self.save()