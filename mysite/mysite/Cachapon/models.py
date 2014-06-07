from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ImageTest(models.Model):
    image1 = models.ImageField(upload_to='Cachapon/images/')

class Pet(models.Model):

	name = models.CharField( max_length=20)
	icon = models.ImageField(upload_to='Cachapon/icons/')
	picture = models.ImageField(upload_to='Cachapon/pictures/')
	attribute = models.CharField( max_length=8)
	rare = models.CharField( max_length=6)
	attack = models.IntegerField()
	health = models.IntegerField()
	recover = models.IntegerField()

	active_skill = models.ForeignKey('Skill',related_name='active_skill')
	leader_skill = models.ForeignKey('Skill',related_name='leader_skill')

	def icon_tag(self):
		return u'<img src="/media/%s" height=50 width=50/>' %self.icon
	
	icon_tag.allow_tags = True

	def __unicode__(self):
	    return self.name


class Skill(models.Model):
	name = models.CharField(default='no definetion', max_length=20)
	info = models.TextField(default='no description')

	def __unicode__(self):
	    return self.name

class Record(models.Model):
	player = models.ForeignKey(User)
	pet = models.ForeignKey('Pet')
	date = models.DateField()

	def __unicode__(self):
		return self.player.username + ": " + self.pet.name
