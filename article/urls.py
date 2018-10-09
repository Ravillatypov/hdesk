from django.urls import path
from article.views import addComment, addTag, addCategory, indexPage, viewArticle, editArticle
urlpatterns = [
    path('<int:pk>/', viewArticle, name='kb'),
    path('comment/<int:pk>', addComment, name='comment'),
    path('edit/<int:pk>', editArticle, name='edit'),
    path('new', editArticle, name='new_article'),
    path('tag', addTag, name='tag_form'),
    path('category', addCategory, name='category_form'),
    path('', indexPage),
]