from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect, render_to_response


from .forms import ArticleForm
from .models import Article


def article_list(request):
    """
    Unlike in post_list, articles list does not show text when watching the list
    User has to enter into the article_detail view to read the text
    """
    articles = Article.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'articles/article_list.html', {'articles':articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'articles/article_detail.html', {'article': article})


def article_new(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.published_date = timezone.now()
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, 'articles/article_edit.html', {'form':form})


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.modified_date = timezone.now() #This will be shown instead of published date after editing
            article.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_edit.html', {'form':form})
