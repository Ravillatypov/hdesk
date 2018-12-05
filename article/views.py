from article.models import Tag, Comment, Category, Article
from article.forms import TagForm, CategoryForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from datetime import datetime
from app.utils import getBaseContext

@permission_required('article.view_comment', login_url='/login')
@permission_required('article.view_category', login_url='/login')
@permission_required('article.view_tag', login_url='/login')
def viewArticle(request, pk=None):
    context = getBaseContext()
    if pk is not None:
        try:
            arts = Article.objects.get(pk=pk)
            art_comments = Comment.objects.filter(article=arts)
            art_tags = arts.tag.all()
        except Exception:
            arts = None
            art_comments = None
            art_tags = None
        context.update({'art': arts, 'comments': art_comments, 'arttags': art_tags})
        return render(request, 'article.html', context)

@permission_required('article.add_comment', login_url='/login')
def addComment(request, pk=None):
    if pk is None or request.method == 'GET':
        return redirect('/')
    art = Article.objects.get(pk=pk)
    comment = request.POST.get('comment')
    com = Comment(comment=comment, author=request.user, article=art)
    com.save()
    return redirect('kb', pk=pk)

@permission_required('article.add_article', login_url='/login')
@permission_required('article.change_article', login_url='/login')
def editArticle(request, pk=0):
    context = getBaseContext()
    if pk == 0:
        art = Article(author=request.user, title='новая статья')
        art.pk = 0
    else:
        art = Article.objects.get(pk=pk)
        tags = [t.title for t in art.tag.all()]
        art.taglist = ','.join(tags)
    if request.method == 'GET':
        context.update({'pk': art.pk, 'art': art, 'arttags': art.tag.all()})
        return render(request, 'article-edit.html', context)
    if request.method == 'POST':
        if pk == 0:
            art = Article.objects.create(author=request.user, title='новая статья')
        catname = request.POST.get('category')
        category,_ = Category.objects.get_or_create(title=catname)
        art.tag.clear()
        for tagname in request.POST.get('tag').split(','):
            if len(tagname)>0:
                tag,_ = Tag.objects.get_or_create(title=tagname)
                art.tag.add(tag)
        art.author = request.user
        art.title = request.POST.get('title')
        art.post = request.POST.get('post')
        art.category = category
        art.save()
        return redirect('kb', pk=art.pk)

@permission_required('article.add_tag', login_url='/login')
def addTag(request):
    if request.method == 'POST':
        form = TagForm(request.POST, prefix='tag')
        if form.is_valid():
            form.save()
    return redirect('/')

@permission_required('article.add_category', login_url='/login')
def addCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, prefix='cat')
        if form.is_valid():
            form.save()
    return redirect('/')