from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
	
	email = forms.EmailField(required=True)
	#stone = forms.IntegerField(widget=forms.HiddenInput,initial=50)

	class Meta:
		model = User
		fields = ('username', 'password1', 'password2' , 'email')

	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		#user.stone = self.cleaned_data['stone']

		if commit:
			user.save()

		return user