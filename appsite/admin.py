from django.contrib import admin
from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'date', 'is_replied')
    search_fields = ('nom', 'email', 'contenu')
    readonly_fields = ('nom', 'email', 'contenu', 'date', 'is_replied')
    fields = ('nom', 'email', 'contenu', 'date', 'response', 'is_replied')

    def save_model(self, request, obj, form, change):
        if obj.response and not obj.is_replied:
            try:
                send_mail(
                    subject="Réponse à votre message",
                    message=obj.response,
                    from_email='ton@email.com',  # Remplace par ton e-mail
                    recipient_list=[obj.email],
                )
                obj.is_replied = True
                self.message_user(request, f"Réponse envoyée à {obj.email}", level=messages.SUCCESS)
            except Exception as e:
                self.message_user(request, f"Erreur d'envoi : {str(e)}", level=messages.ERROR)

        super().save_model(request, obj, form, change)








