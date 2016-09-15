from django.db import models
from django.utils import timezone


class Entry(models.Model):
    author = models.ForeignKey('auth_ex.User')
    title = models.CharField(max_length=200)
    text= models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    modified_date = models.DateTimeField(null=True)
    comment_count = models.IntegerField(blank=True, default=0)


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self):
        return self.title

