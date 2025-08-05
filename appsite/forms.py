from django import forms
from .models import ContactMessage  # Assure-toi que le modèle est importé

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['nom', 'email', 'contenu']
        widgets = {
            'contenu': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'nom': 'Nom',
            'email': 'Email',
            'contenu': 'Message',
        }
