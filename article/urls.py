from django.urls import path
from article.views import Tags,Categories, ArticleView, mainView, addComment
urlpatterns = [
    path('tapi/ags', Tags.as_view()),
    path('api/categories', Categories.as_view()),
    path('api/article', ArticleView.as_view()),
    path('<int:pk>/', mainView, name='kb'),
    path('comment/<int:pk>', addComment, name='comment'),
    path('', mainView),
]