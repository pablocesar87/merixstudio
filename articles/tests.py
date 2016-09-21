import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Article


class ArticleMethodTests(TestCase):

    def test_was_published_recently_with_future_article_date(self):
        """
        was_published_recently() should return False for articles whose
        published_date is in the future.
         """
        time = timezone.now() + datetime.timedelta(days=30)
        future_article = Article(published_date=time)
        self.assertIs(future_article.was_published_recently(), False)

    def test_was_published_recently_with_old_article(self):
        """
        was_published_recently() should return False for articles whose
        published_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=30)
        old_article = Article(published_date=time)
        self.assertIs(old_article.was_published_recently(), False)

    def test_was_published_recently_with_recent_article(self):
        """
        was_published_recently() should return True for articles whose
        published_date is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=1)
        recent_article = Article(published_date=time)
        self.assertIs(recent_article.was_published_recently(), True)


def create_article(title, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Article.objects.create(title=title, published_date=time)


class EntryViewTests(TestCase):
    def test_list_view_with_no_articles(self):
        """
        If no articles exist, an appropriate message should be displayed.
        """
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No articles are available.")
        self.assertQuerysetEqual(response.context['articles'], [])

    def test_list_view_with_a_past_article(self):
        """
        Articles with a published_date in the past should be displayed on the
        article_list page.
        """
        create_article(title='past article', days=-30)
        response = self.client.get('/articles/')
        self.assertQuerysetEqual(
            response.context['articles'],
            ['<Article: past article>']
        )

    def test_list_view_with_a_future_article(self):
        """
        Articles with a published_date in the future should not be displayed on
        the article_list page.
        """
        create_article(title=" future article", days=30)
        response = self.client.get('/articles/')
        self.assertContains(response, "No articles are available.")
        self.assertQuerysetEqual(response.context['articles'], [])

    def test_list_view_with_future_article_and_past_article(self):
        """
        Even if both past and future articles exist, only past articles
        should be displayed.
        """
        create_article(title="past article", days=-30)
        create_article(title="future article", days=30)
        response = self.client.get('/articles/')
        self.assertQuerysetEqual(
            response.context['articles'],
            ['<Article: past article>']
        )

    def test_list_view_with_two_past_articles(self):
        """
        The article list page may display multiple articles.
        """
        create_article(title="past article", days=-30)
        create_article(title="past article 2", days=-5)
        response = self.client.get('/articles/')
        self.assertQuerysetEqual(
            response.context['articles'],
            ['<Article: past article>', '<Article: past article 2>']
        )
