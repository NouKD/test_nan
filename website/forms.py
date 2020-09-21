from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):


    nom = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'name',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'email address',
    }))

    sujet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'sujet',
    }))

    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Message',
        'name': '',
        'id': '',
        'cols': '30',
        'rows': '7',
    }))

    class Meta:
        model = Contact
        fields = ['nom', 'email', 'sujet', 'message']