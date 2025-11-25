from django.db import models
from django.contrib.auth.models import User

# ------------------------------
# NGO Model
# ------------------------------
class NGO(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# ------------------------------
# Medicine Model
# ------------------------------
class Medicine(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    expiry_date = models.DateField()
    image = models.ImageField(upload_to='medicine/')
    donated = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# ------------------------------
# Donation Model
# ------------------------------
class Donation(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('RECEIVED', 'Received'),
    ]

    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    ngo = models.ForeignKey(NGO, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.medicine.name} → {self.ngo.name}"
