from django.db import models
from django.contrib.auth.models import AbstractUser

class Utilisateur(AbstractUser):
    ROLE_MEDECIN = 'medecin'
    ROLE_ASSISTANT = 'assistant'
    ROLE_CHOICES = [
        (ROLE_MEDECIN, 'Médecin'),
        (ROLE_ASSISTANT, 'Assistant'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, editable=False, db_index=True)
    adresse = models.TextField(blank=True, null=True)
    numero_telephone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.get_full_name()} - {self.get_full_name()}"
    
    def save(self, *args, **kwargs):
        if not self.role and not self.is_superuser:
            raise ValueError("Le champ 'role' est obligatoire pour les utilisateurs non superutilisateurs.")
        super().save(*args, **kwargs)

class Medecin(Utilisateur):
    specialite = models.CharField(max_length=100)
    class Meta:
        verbose_name = "Médecin"
        verbose_name_plural = "Médecins"
    def save(self, *args, **kwargs):
        self.role = self.ROLE_MEDECIN
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Dr. {self.get_full_name()} - {self.specialite}"
    
class Assistant(Utilisateur):
    class Meta:
        verbose_name = "Assistant"
        verbose_name_plural = "Assistants"
    def save(self, *args, **kwargs):
        self.role = self.ROLE_ASSISTANT
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.get_full_name()} - {self.role}"