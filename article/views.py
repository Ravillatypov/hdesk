from article.models import Tag, Comment, Category, Article
from django.shortcuts import render, redirect

def mainView(request, pk=None):
    context = getBaseContext()
    if pk is not None:
        try:
            arts = Article.objects.get(pk=pk)
            art_comments = Comment.objects.filter(article=arts)
        except Exception:
            arts = None
            art_comments = None
        context.update({'art': arts, 'comments': art_comments, 'arttags': arts.tag.all()})
        return render(request, 'article.html', context)
    return render(request, 'index.html', context)

def addComment(request, pk=None):
    if pk is None or request.method == 'GET':
        return redirect('/')
    art = Article.objects.get(pk=pk)
    comment = request.POST.get('comment')
    com = Comment(comment=comment, author=request.user, article=art)
    com.save()
    return redirect('kb', pk=pk)

def ArticleEdit(request, pk=0):
    context = getBaseContext()
    if pk == 0:
        title = request.user.last_name + ': новая статья'
        art = Article.objects.create(author=request.user, title=title)
    else:
        art = Article.objects.get(pk=pk)
    if request.method == 'GET':
        context.update({'pk': art.pk, 'art': art, 'arttags': art.tag.all()})
        return render(request, 'article-edit.html', context)
    if request.method == 'POST':
        cat_id = request.POST.get('category')
        category = Category.objects.get(pk=cat_id)
        art.tag.clear()
        for tag_id in request.POST.getlist('tag'):
            tag = Tag.objects.get(pk=tag_id)
            art.tag.add(tag)
        art.author = request.user
        art.title = request.POST.get('title')
        art.post = request.POST.get('post')
        art.category = category
        art.save()
        return redirect('kb', pk=art.pk)

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
    return {'tags': tags, 'categories': categories, 'menu': menu}
