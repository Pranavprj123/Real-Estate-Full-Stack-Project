from django import forms
from .models import  Property, PropertyImage

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'city', 'address', 'bhk', 'main_image']


class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']

# class ChatMessageForm(forms.ModelForm):
#     class Meta:
#         model = ChatMessage
#         fields = ['message']
#         widgets = {
#             'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type a message...'})
#         }
