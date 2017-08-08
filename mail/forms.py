from .models import *
from django import forms

class MailForm(forms.ModelForm):
	class Meta:
		model = Mail
		fields =('Receiver','Subject','Message')