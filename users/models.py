from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, blank=True, null=True)  # Ahora es opcional

    ROLE_CHOICES = [
        (1, 'Administrator'),
        (2, 'Coordinator'),
        (3, 'Data Entry'),
        (4, 'Agent'),
    ]
    role_id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=4)
    dni = models.CharField(max_length=15, unique=True)
    phone = models.CharField(max_length=15, blank=True)
    department = models.CharField(max_length=50, blank=True)
    birth_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Generar automáticamente el username si no está definido
        if not self.username:
            base_username = f"{self.first_name.lower()}{self.last_name.lower()}"
            existing_users = User.objects.filter(username__startswith=base_username).count()
            self.username = f"{base_username}{existing_users + 1}" if existing_users else base_username
        super().save(*args, **kwargs)