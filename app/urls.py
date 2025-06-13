from django.urls import path
from app.views import (ArticleCreateView,
                       ArticleListView,
                       ArticleDeleteView,
                       ArticleUpdateView)


urlpatterns = [
    path('create',
         ArticleCreateView.as_view(),
         name='create_article'),
    path('update/<int:pk>',
         ArticleUpdateView.as_view(),
         name='update_article'),
    path('delete/<int:pk>',
         ArticleDeleteView.as_view(),
         name='delete_article'),
    path('',
         ArticleListView.as_view(),
         name='create_article'),
]
