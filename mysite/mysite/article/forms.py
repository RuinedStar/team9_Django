from django import forms
from mysite.article.models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
