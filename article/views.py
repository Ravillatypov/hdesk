from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from article.models import Tag, Comment, Category, Article
from article.serializers import TagSerializer, CommentSerializer, CategorySerializer, ArticleSerializer
from django.shortcuts import render, redirect

class Tags(APIView):
    """Теги"""
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response({"data": serializer.data})

class Categories(APIView):
    """Категории"""
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"data": serializer.data})

class ArticleView(APIView):
    """просмотр статьи"""
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        pk = request.GET.get("id")
        category = request.GET.get("cat")
        tag = request.GET.get("tag")
        if pk is not None:
            art = Article.objects.get(pk=pk)
            serializer = ArticleSerializer(art)
            return Response({"data": serializer.data})
        if category is not None:
            art = Article.objects.get(category=category)
            serializer = ArticleSerializer(art)
            return Response({"data": serializer.data})
        if tag is not None:
            art = Article.objects.get(tag=tag)
            serializer = ArticleSerializer(art)
            return Response({"data": serializer.data})

def mainView(request, pk=None):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    menu = []
    articles = Article.objects.all()
    for category in categories:
        category.items = []
        for art in articles:
            if category == art.category:
                category.items.append(art)
        menu.append(category)
    
    if pk is not None:
        arts = Article.objects.get(pk=pk)
        art_comments = Comment.objects.filter(article=arts)
        return render(request, 'article.html', {'tags': tags, 
        'categories': categories, 'art': arts, 'menu': menu, 
        'comments': art_comments, 'arttags': art.tag.all()})
    return render(request, 'index.html', {'tags': tags, 'categories': categories, 'menu': menu})

def addComment(request, pk=None):
    if pk is None or request.method == 'GET':
        return redirect('/')
    art = Article.objects.get(pk=pk)
    comment = request.POST.get('comment')
    com = Comment(comment=comment, author=request.user, article=art)
    com.save()
    return redirect('kb', pk=pk)