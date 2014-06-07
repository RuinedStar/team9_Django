from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from mysite.Cachapon.models import Record


def ImageTest(request):
    return render_to_response('test.html')

@login_required(login_url='/accounts/login/')
def LookMyBag(request):
	pass
	#petlist = Records.objects.filter(Records.player.id = request.User.id)

	#return render_to_response('articles.html',
	 #                        {'articles': Article.objects.all().order_by('-pub_date')})
