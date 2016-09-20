from __future__ import absolute_import

from celery.decorators import task
from articles.models import Article



@task
def one_new_comment_article(pk):
    object = Article.objects.get(pk=pk)
    object.new_comment()

