from django import forms
from .models import Callback


class CallBackForm(forms.ModelForm):
    class Meta:
        model = Callback
        fields = ('name', 'telephon', 'email', 'message' )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'telephon': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
