from django.urls import path
from article.views import mainView, addComment, ArticleEdit
urlpatterns = [
    path('<int:pk>/', mainView, name='kb'),
    path('comment/<int:pk>', addComment, name='comment'),
    path('edit/<int:pk>', ArticleEdit, name='edit'),
    path('', mainView),
]