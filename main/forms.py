from django import forms
from .models import Callback


class CallBackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = ('name', 'telephon')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'telephon': forms.TextInput(attrs={'class': 'form-control'}),
        }
