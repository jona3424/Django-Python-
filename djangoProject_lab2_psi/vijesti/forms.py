from django import forms
from django.core.exceptions import ValidationError

from .models import *
from django.contrib.auth.forms import UserCreationForm

class SearchForm(forms.Form):
     term = forms.CharField(max_length=50, required=True)
     group = forms.ChoiceField(choices=[
         ('mod', 'Moderator'),
         ('default', 'Default'),
         ],
        required=True, widget=forms.RadioSelect, initial=[0])
class KorisnikCreateForm(UserCreationForm):
    class Meta:
        model=Korisnik
        fields= ['username','password1','password2','email','last_name','first_name']



class VijestForm(forms.ModelForm):
    class Meta:

        model=Vijest
        exclude=['autor']