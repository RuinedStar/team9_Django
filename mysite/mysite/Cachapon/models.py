from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save

# Create your models here.

class Pet(models.Model):

	name = models.CharField( max_length=20)
	icon = models.ImageField(upload_to='Cachapon/icons/')
	picture = models.ImageField(upload_to='Cachapon/pictures/')
	attribute = models.CharField( max_length=8)
	rare = models.IntegerField()
	attack = models.IntegerField()
	health = models.IntegerField()
	recover = models.IntegerField()

	active_skill = models.ForeignKey('Skill',related_name='active_skill')
	leader_skill = models.ForeignKey('Skill',related_name='leader_skill')

	def icon_tag(self):
		return u'<img src="/media/%s" height=50 width=50/>' %self.icon
	
	icon_tag.allow_tags = True

	def __unicode__(self):
		return unicode(self.name)


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
		return self.player.username + " : " + self.pet.name
	

class Prize(models.Model):
	pet = models.ForeignKey('Pet')
	weight = models.IntegerField(validators=[MinValueValidator(1),
											 MaxValueValidator(100)])
	godfest = models.BooleanField(default = False)

	def __unicode__(self):
		return self.pet.name + " : " + str(self.weight)

class Profile(models.Model):
	user = models.OneToOneField(User)
	cash = models.IntegerField(default=50)
	
	def __unicode__(self):
		return str(self.cash) + " stone, " + self.user.username

	def user_post_save(sender, instance, created, **kwargs):
	#Create a user profile when a new user account is created
	    if created == True:
	        p = Profile()
	        p.user = instance
	        p.save()

	post_save.connect(user_post_save, sender=User)