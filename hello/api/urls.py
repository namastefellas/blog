from django.urls import path, include

from api.views.articles import (
ArticleView, 
ArticleDetailView,
ArticleUpdateView, 
ArticleCreateView,
ArticleDeleteView
)


app_name = 'api'

article_urls = [
    path('', ArticleView.as_view(), name='articles'),
    path('<create>', ArticleCreateView.as_view(), name='articles_create'),
    path('<int:pk>/update', ArticleUpdateView.as_view(), name='articles_update'),
    path('<int:pk>/detail', ArticleDetailView.as_view(), name='articles_detail'),
    path('<int:pk>/delete', ArticleDeleteView.as_view(), name='articles_delete')

]

urlpatterns = [
    path('articles/', include(article_urls))
]