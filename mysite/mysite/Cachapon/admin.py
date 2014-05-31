from django.contrib import admin
from mysite.Cachapon.models import ImageTest,Pet, Skill

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
	list_display = ('icon_tag','name', 'health', 'attack', 'recover')

admin.site.register(ImageTest)
admin.site.register(Pet, AuthorAdmin)
admin.site.register(Skill)

