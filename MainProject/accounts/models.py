from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AgentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_agent_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('agent', 'Agent'),
        ('customer', 'Customer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    is_agent_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
