import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Entry


class EntryMethodTests(TestCase):

    def test_was_published_recently_with_future_post_date(self):
        """
        was_published_recently() should return False for posts whose
        published_date is in the future.
         """
        time = timezone.now() + datetime.timedelta(days=30)
        future_post = Entry(published_date=time)
        self.assertIs(future_post.was_published_recently(), False)

    def test_was_published_recently_with_old_post(self):
        """
        was_published_recently() should return False for posts whose
        published_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_post = Entry(published_date=time)
        self.assertIs(old_post.was_published_recently(), False)

    def test_was_published_recently_with_recent_post(self):
        """
        was_published_recently() should return True for posts whose
        published_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_post = Entry(published_date=time)
        self.assertIs(recent_post.was_published_recently(), True)


def create_post(title, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Entry.objects.create(title=title, published_date=time)


class EntryViewTests(TestCase):

    def test_list_view_with_no_posts(self):
        """
        If no posts exist, an appropriate message should be displayed.
        """
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_list_view_with_a_past_post(self):
        """
        Posts with a published_date in the past should be displayed on the
        post_list page.
        """
        create_post(title='past post', days=-30)
        response = self.client.get('/blog/')
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Entry: past post>']
        )

    def test_list_view_with_a_future_post(self):
        """
        Posts with a published_date in the future should not be displayed on
        the post_list page.
        """
        create_post(title=" future post", days=30)
        response = self.client.get('/blog/')
        self.assertContains(response, "No posts are available.")
        self.assertQuerysetEqual(response.context['posts'], [])

    def test_list_view_with_future_post_and_past_post(self):
        """
        Even if both past and future posts exist, only past posts
        should be displayed.
        """
        create_post(title="past post", days=-30)
        create_post(title="future post", days=30)
        response = self.client.get('/blog/')
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Entry: past post>']
        )

    def test_list_view_with_two_past_posts(self):
        """
        The posts list page may display multiple posts.
        """
        create_post(title="past post", days=-30)
        create_post(title="past post 2", days=-5)
        response = self.client.get('/blog/')
        self.assertQuerysetEqual(
            response.context['posts'],
            ['<Entry: past post>', '<Entry: past post 2>']
        )
