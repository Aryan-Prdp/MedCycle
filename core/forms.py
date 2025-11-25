from django import forms
from .models import Medicine
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# ------------------------------
# Medicine Form
# ------------------------------
class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'quantity', 'expiry_date', 'image']


# ------------------------------
# Registration Form
# ------------------------------
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
