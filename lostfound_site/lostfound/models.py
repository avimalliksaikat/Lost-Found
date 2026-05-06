from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class LostItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class LostItem(models.Model):
    TYPE_CHOICES = [
        ('ID Card', 'ID Card'),
        ('Wallet', 'Wallet'),
        ('Book', 'Book'),
        ('Phone', 'Phone'),
        ('Other', 'Other'),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.type} - {self.location}"


class FoundItem(models.Model):
    TYPE_CHOICES = [
        ('ID Card', 'ID Card'),
        ('Wallet', 'Wallet'),
        ('Book', 'Book'),
        ('Phone', 'Phone'),
        ('Other', 'Other'),
    ]

    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    description = models.TextField()
    location = models.CharField(max_length=200)
    contact = models.CharField(max_length=50)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.type} - {self.location}"