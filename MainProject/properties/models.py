from django.db import models
from django.contrib.auth.models import User

BHK_CHOICES = (
    ('1', '1 BHK'),
    ('2', '2 BHK'),
    ('3', '3 BHK'),
    ('4', '4 BHK'),
)

class Property(models.Model):
    title = models.CharField(max_length=200, default="No Title")
    description = models.TextField(default="No Description")
    price = models.IntegerField(default=0)
    city = models.CharField(max_length=100, default="Unknown")
    state = models.CharField(max_length=100, default="Unknown")
    address = models.CharField(max_length=255, default="Not Available")
    bhk = models.IntegerField(default=1)
    main_image = models.ImageField(upload_to='properties/', blank=True, null=True)
    
    property_type = models.CharField(max_length=50, default="Apartment")
    furnished = models.CharField(max_length=50, default="Unfurnished")
    amenities = models.TextField(default="")

    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name="properties")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    property = models.ForeignKey(Property, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="property_extra/")

    def __str__(self):
        return f"Image for {self.property.title}"


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'property')

    def __str__(self):
        return f"{self.user.username} -> {self.property.title}"

