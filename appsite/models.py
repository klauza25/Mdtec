from django.db import models

class ContactMessage(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    contenu = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    response = models.TextField(blank=True, null=True)
    is_replied = models.BooleanField(default=False, verbose_name="Réponse")

    def __str__(self):
        return f"{self.nom} ({self.email})"
