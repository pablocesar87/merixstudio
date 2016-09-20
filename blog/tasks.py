from __future__ import absolute_import

from celery.decorators import task
from blog.models import Entry



@task
def one_new_comment_blog(pk):
    object = Entry.objects.get(pk=pk)
    object.new_comment()

