from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from article.models import Tag, Comment, Category, Article
from article.serializers import TagSerializer, CommentSerializer, CategorySerializer, ArticleSerializer
from django.shortcuts import render

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

def mainView(request):
    categories = Category.objects.all()
    tags = Tag.objects.all()
    category = request.GET.get("cat")
    tag = request.GET.get("tag")
    pk = request.GET.get("id")
    if pk is not None:
        arts = Article.objects.get(pk=pk)
        return render(request, 'article.html', {'tags': tags, 'categories': categories, 'art': arts})
    if category is not None:
        arts = Article.objects.filter(category=category)
        return render(request, 'articles-categories.html', {'tags': tags, 'categories': categories, 'arts': arts})
    if tag is not None:
        arts = Article.objects.filter(tag=tag)
        return render(request, 'articles-tags.html', {'tags': tags, 'categories': categories, 'arts': arts})
    return render(request, 'index.html', {'tags': tags, 'categories': categories})
