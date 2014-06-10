from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from mysite.Cachapon.models import Record, Prize
from datetime import datetime

def Home(request):
    return render_to_response('Cachapon/index.html')

@login_required(login_url='/accounts/login/')
def LookYourBox(request):
	records = Record.objects.filter(player = request.user)
	pets = []
	for record in records:
		icon_url = "/media/" + str(record.pet.icon)
		pets.append(icon_url)

	return render_to_response('Cachapon/box.html', {'pets' : pets })

@login_required(login_url='/accounts/login/')
def CachaEgg(request):

	if request.method == 'POST':
		prize = Prize.objects.get(pk=1)
		record = Record(player = request.user, pet = prize.pet, date = datetime.today())
		record.save()
		return HttpResponseRedirect('/Cachapon/bag/')
	c = {}
	c.update(csrf(request))
	return render_to_response('Cachapon/gacha.html', c)