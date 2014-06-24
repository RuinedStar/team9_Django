# -*- coding: utf-8 -*-

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

	p = Profile.objects.filter(user = request.user).get()
	msg = ''
	icon = ''

	if request.method == 'POST':
		if p.cash < 5:
			msg = u'剩餘的魔法石數量不足, 請確定數量後再試'
		else :
			p.cash -= 5
			p.save()
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
			icon = prizePet.icon

	c = {}
	c["cashes"] = p.cash
	c["error"] = msg
	c["icon"] = icon
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
	icons = Record.objects.filter(player = request.user).values_list('pet__id','pet__icon')
	ids = Record.objects.filter(player = request.user).values_list('pet',flat=True).distinct()
	infos = Pet.objects.filter(pk__in=ids)

	return render_to_response('Cachapon/box.html', {'icons' : icons, 'infos' : infos})

