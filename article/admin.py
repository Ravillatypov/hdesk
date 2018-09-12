from django.contrib import admin
from article.models import Article, Category, Tag, Comment
from django_summernote.admin import SummernoteModelAdmin

class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

    def save_model(self, request, instance, form, change):
        user = request.user 
        instance = form.save(commit=False)
        if not change or not instance.author:
            instance.author = user
        instance.save()
        form.save_m2m()
        return instance


admin.site.register(Comment, ArticleAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)

