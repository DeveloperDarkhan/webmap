from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    UpdateView,
)
from .models import Article
from django.urls import reverse_lazy

# Create your views here.

class ArticleListView(ListView):
    template_name = 'article_list.html'
    # template_name = 'alternate_article_list.html'
    
    model = Article

class ArticleDetailView(DetailView):
    template_name = 'detail_article.html'

class ArticleUpdateView(UpdateView):
    template_name = 'update_article.html'
    model = Article
    fields = ['title', 'body']

class ArticleDeleteView(DeleteView):
    template_name = 'delete_article.html'
    model = Article
    success_url = reverse_lazy('home')

class ArticleCreateView(CreateView):
    template_name = 'create_article.html'
    model = Article
    fields = '__all__'