from django.contrib import admin
from mysite.Cachapon.models import ImageTest, Pet, Skill, Record, Prize

# Register your models here.

class AuthDisplay(admin.ModelAdmin):
	list_display = ('icon_tag','name', 'health', 'attack', 'recover')

admin.site.register(ImageTest)
admin.site.register(Pet, AuthDisplay)
admin.site.register(Skill)
admin.site.register(Record)
admin.site.register(Prize)
