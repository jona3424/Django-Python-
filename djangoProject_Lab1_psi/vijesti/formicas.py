from django.forms import forms

from django.forms import CharField
class VestForm(forms.Form):
    autor = CharField(label='autor', max_length=32)
    sadrzaj = CharField(label='sadrzaj', max_length=99)


