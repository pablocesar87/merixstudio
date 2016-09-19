from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

from .forms import CommentForm
from .models import Comment
from blog.models import Entry
from articles.models import Article
from blog.views import post_detail
from articles.views import article_detail



def article_new_comment(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.created_date=timezone.now()
            comment.save()
            return redirect(article_detail, pk=article.pk)
    else:
        form=CommentForm()
    return render(request, 'comments/add_new_comment.html', {'form': form})



def blog_new_comment(request, pk):
    post = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.created_date = timezone.now()
            comment.save()
            return redirect(post_detail, pk=post.pk)
    else:
        form=CommentForm()
    return render(request, 'comments/add_new_comment.html', {'form': form})





