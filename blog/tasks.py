from __future__ import absolute_import

from celery.decorators import task
from blog.models import Entry

'''
This task is calling the new_comment method of the object
and adding it to the queue. At the moment there is a known bug:
If admin deletes or adds comments from the admin site, those
comments are not taking into account.
'''


@task
def one_new_comment_blog(pk):
    obj = Entry.objects.get(pk=pk)
    obj.new_comment()
