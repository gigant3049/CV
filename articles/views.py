from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from articles.forms import CommentForm
from articles.models import Article, Comment


def detail(request, slug, *args, **kwargs):
    form = CommentForm()
    article = get_object_or_404(Article, slug=slug)
    articles = Article.objects.order_by("-id")[:3]
    q = request.GET.get('q')
    comments = Comment.objects.filter(article_id=article.id, top_level_comment_id__isnull=True)
    if q:
        q = Q(title__icontains=q)
        articles = Article.objects.filter(q).order_by('-id')

    cid = request.GET.get('cid')
    if request.method == "POST":
        comment = CommentForm(request.POST, request.FILES)
        if comment.is_valid():
            comment = comment.save(commit=False)
            comment.article = article
            comment.parent_id = cid
            comment.save()
            messages.success(request, 'Your comment has been submitted successfully.')
            return redirect('.#comment-form-reply')
    else:
        form = CommentForm()

    ctx = {
        'form': form,
        'article': article,
        'articles': articles,
        'comments': comments
    }
    return render(request, 'single.html', ctx)
