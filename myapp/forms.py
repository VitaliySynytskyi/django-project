from django import forms
from .models import Logs

class Form1(forms.ModelForm):
    class Meta:
        model= Logs
        fields= ["name", "number", "action"]