from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from mysite.article.models import Article
from mysite.article.forms import ArticleForm

from django.contrib.auth.decorators import login_required

# Create your views here.

def articles(request):
    return render_to_response('articles.html',
                             {'articles': Article.objects.all()})

def article(request, article_id=1):
    return render_to_response('article.html',
                             {'article': Article.objects.get(id=article_id)})


@login_required(login_url='/accounts/login/')
def create(request):
    if request.POST:
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('articles/all')

    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('create_article.html', args)

def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()

    return HttpResponseRedirect('/articles/get/%s' %article_id)