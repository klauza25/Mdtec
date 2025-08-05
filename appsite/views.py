from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    message_envoye = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Sauvegarde l'objet ContactMessage directement
            message_envoye = True
            form = ContactForm()  # Reset formulaire vide après envoi réussi
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'message_envoye': message_envoye
    })

def success_view(request):
    return render(request, 'success.html')


   