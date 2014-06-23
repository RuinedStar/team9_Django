from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from mysite.Cachapon.models import Record, Prize, Profile, Pet
from datetime import datetime
import bisect, random

def Home(request):
    return render_to_response('Cachapon/index.html')

@login_required(login_url='/accounts/login/')
def CachaEgg(request):

	if request.method == 'POST':
		prizes = Prize.objects.values_list('pet','weight')
		pweights = [prize[1] for prize in prizes]
		aggreSum = 0
		for i,j in enumerate(pweights):
			aggreSum += j
			pweights[i] = aggreSum
		rnd = random.randint(1, aggreSum)
		result = bisect.bisect_left(pweights, rnd)
		prizePet = Pet.objects.get(pk=prizes[result][0])
		record = Record(player = request.user, pet = prizePet, date = datetime.today())
		record.save()

	c = {}
	c.update(csrf(request))
	return render_to_response('Cachapon/cacha.html', c)

@login_required(login_url='/accounts/login/')
def Shop(request):

	pdict = {"stone0":1, "stone1":6, "stone2":12,"stone3":30,"stone4":60,"stone5":85}

	p = Profile.objects.filter(user = request.user).get()

	for key in pdict.keys():
		if request.POST.get(key) is not None:
			p.cash += pdict[key]
			p.save()
			break

	c = {}
	c.update(csrf(request))
	c["cashes"] = p.cash
	return render_to_response('Cachapon/shop.html', c)

@login_required(login_url='/accounts/login/')
def LookYourBox(request):
	records = Record.objects.filter(player = request.user)
	pets = []
	for record in records:
		icon_url = "/media/" + str(record.pet.icon)
		pets.append(icon_url)

	return render_to_response('Cachapon/box.html', {'pets' : pets })

