from django.urls import path
from article.views import *
urlpatterns = [
    path('tags', Tags.as_view()),
    path('categories', Categories.as_view()),
    path('article', ArticleView.as_view()),
]