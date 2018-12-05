from article.models import Tag, Comment, Category, Article
from django.shortcuts import render
from article.forms import TagForm, CategoryForm

def getBaseContext():
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
    tagform = TagForm(prefix='tag')
    catform = CategoryForm(prefix='cat')
    return {'tags': tags, 'categories': categories, 
            'artmenu': menu}

def indexPage(request):
    context = getBaseContext()
    return render(request, 'index.html', context)