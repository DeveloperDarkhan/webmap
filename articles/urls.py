from django.urls import path
from .views import (
    ArticleListView,
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
)

urlpatterns =[
    path('article/create/', ArticleCreateView.as_view(), name='create_article'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name = 'update_article'),
    path('article/<int:pk>/detail/', ArticleDetailView.as_view(), name = 'detail_article'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name = 'delete_article'),
    path('article/<int:pk>/', ArticleCreateView.as_view(), name = 'edit_article'),
    path('', ArticleListView.as_view(), name ='article_list'),
]