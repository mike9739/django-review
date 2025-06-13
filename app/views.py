from app.models import Article
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy


def index(request):
    articles = Article.objects.all()
    return render(request, "app/article.html", {"articles": articles})


class ArticleListView(ListView):
    template_name = 'app/articles.html'
    model = Article
    context_object_name = 'articles'


class ArticleCreateView(CreateView):
    template_name = 'app/article_create.html'
    model = Article
    fields = ['title', 'status', 'content', 'word_count', 'twitter_post']
    success_url = reverse_lazy('articles')


class ArticleUpdateView(UpdateView):
    template_name = 'app/article_update.html'
    model = Article
    fields = ['title', 'status', 'content', 'word_count', 'twitter_post']
    success_url = reverse_lazy('articles')
    context_object_name = "article"


class ArticleDeleteView(DeleteView):
    template_name = 'app/article_delete.html'
    model = Article
    success_url = reverse_lazy('articles')
    context_object_name = "article"
