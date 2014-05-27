from django import forms
from mysite.userprofile.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
    	fields = ('cash','likes_cheese')
