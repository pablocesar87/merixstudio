from django.db import models


class Comment(models.Model):
    '''
    Added generic relationship with the blog nad articles apps
    related_names are needed in order to avoid conflicts
    '''
    post = models.ForeignKey('blog.Entry', related_name='post_comments', blank=True, null=True)
    article = models.ForeignKey('articles.Article', related_name='article_comments', blank=True, null=True)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body