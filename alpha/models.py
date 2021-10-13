from django.db import models
from django.forms import Textarea, TextInput
from django.forms import ModelForm
# Create your models here.
class ContactMessage(models.Model):
    STATUS =(
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )

    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True, max_length=50)
    subject = models.CharField(blank=True, max_length=50)
    message = models.TextField(blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    note = models.CharField(blank=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name or ""


class ContactForm(ModelForm):
    class Meta:
        model= ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        