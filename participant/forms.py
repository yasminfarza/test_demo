from django import forms
from django.forms import Form

class TestForm(Form):
    name = forms.CharField(max_length=50)
    score = forms.IntegerField()