from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from mysite.Cachapon.models import Record, Prize
from datetime import datetime

def ImageTest(request):
    return render_to_response('test.html')

@login_required(login_url='/accounts/login/')
def LookYourBag(request):
	records = Record.objects.filter(player = request.user)
	return render_to_response('bag.html', {'records' : records })

@login_required(login_url='/accounts/login/')
def CachaEgg(request):

	if request.method == 'POST':
		prize = Prize.objects.get(pk=1)
		record = Record(player = request.user, pet = prize.pet, date = datetime.today())
		record.save()
		return HttpResponseRedirect('/Cachapon/bag/')
	c = {}
	c.update(csrf(request))
	return render_to_response('cacha.html', c)