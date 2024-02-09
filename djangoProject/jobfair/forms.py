from django.forms import *


class SearchForm(Form):
    Naziv_konkursa = CharField(max_length=50, required=True)
    CHOICES = [
        ('0', 'Strucna praksa'),
        ('1', 'Zapolenje'),
    ]
    tip = MultipleChoiceField(choices=CHOICES,required=True, widget=CheckboxSelectMultiple, initial=CHOICES)


class VestForm(Form):


    KorisnickoIme = CharField(required=True, max_length=32)

