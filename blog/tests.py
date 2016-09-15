import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Entry


class EntryMethodTest(TestCase):

    def test_was_published_recently_with_future_post_date(self):
        """
        was_published_recently() should return False for posts whose
        published_date is in the future.
         """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Entry(published_date=time)
        self.assertIs(future_post.was_published_recently(), False)
