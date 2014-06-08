from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from mysite.Cachapon.models import Record, Pet


def ImageTest(request):
    return render_to_response('test.html')

@login_required(login_url='/accounts/login/')
def LookYourBag(request):
	records = Record.objects.filter(player = request.user)
	return render_to_response('bag.html', {'records' : records })