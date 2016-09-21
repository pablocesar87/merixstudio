from django.utils import timezone
from django.test import TestCase

from .models import Comment
from articles.models import Article
from blog.models import Entry


class CommentMethodTests(TestCase):

    def test_if_comment_was_added_to_article(self):
        """
        This test will check if comments are being counted for articles
        """
        article = Article()
        number_of_comments = article.get_comment_count()
        article.new_comment()
        later_number_of_comments = article.get_comment_count()
        self.assertIs(number_of_comments < later_number_of_comments, True)

    def test_if_comment_was_added_to_post(self):
        """
        This test will check if comments are being counted for posts
        """
        post = Entry()
        number_of_comments = post.get_comment_count()
        post.new_comment()
        later_number_of_comments = post.get_comment_count()
        self.assertIs(number_of_comments < later_number_of_comments, True)

    def test_if_comment_created_date_is_more_recent_or_equal_than_article_created_date(self):
        """
        This test will check if the created_date for the comment is more recent
        or equal than the article created_date, which should be True
        """
        time_article = timezone.now()
        article = Article(created_date=time_article)
        article_created_date = article.created_date
        time_comment = timezone.now()
        comment = Comment(created_date=time_comment)
        comment_created_date = comment.created_date
        self.assertIs(comment_created_date >= article_created_date, True)

    def test_if_comment_created_date_is_more_recent_or_equal_than_post_created_date(self):
        """
        This test will check if the created_date for the comment is more recent
        or equal than the post created_date, which should be True
        """
        time_post = timezone.now()
        post = Entry(created_date=time_post)
        post_created_date = post.created_date
        time_comment = timezone.now()
        comment = Comment(created_date=time_comment)
        comment_created_date = comment.created_date
        self.assertIs(comment_created_date >= post_created_date, True)
