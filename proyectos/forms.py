from django import forms
from .models import program

class proForm(forms.ModelForm):
    class Meta:
        model = program
        fields = '__all__'