from article.models import Comment, Tag, Category, Article
from django import forms

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('title',)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title',)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title',)