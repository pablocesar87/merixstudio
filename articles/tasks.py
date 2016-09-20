from __future__ import absolute_import

from celery.decorators import task
from articles.models import Article

'''
This task is calling the new_comment method of the object
and adding it to the queue. At the moment there is a known bug:
If admin deletes or adds comments from the admin site, those
comments are not taking into account.
'''


@task
def one_new_comment_article(pk):
    obj = Article.objects.get(pk=pk)
    obj.new_comment()
