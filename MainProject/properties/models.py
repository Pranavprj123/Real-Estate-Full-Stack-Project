from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.




class Property(models.Model):
    PROPERTY_TYPE = (
        ('flat', 'Flat'),
        ('house', 'House'),
        ('office', 'Office'),
    )

    AMENITIES_CHOICES = (
        ('parking', 'Parking'),
        ('lift', 'Lift'),
        ('security', 'Security'),
        ('furnished', 'Furnished'),
        ('balcony', 'Balcony'),
        ('powerbackup', 'Power Backup'),
    )

    
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPE)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    furnished = models.BooleanField(default=False)
    amenities = MultiSelectField(choices=AMENITIES_CHOICES, max_length=200, blank=True)
    status = models.CharField(max_length=20, default="available")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.property.title}"
    
class ChatMessage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # 👈 NEW

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.sender} → {self.receiver} | {self.property.title}"
