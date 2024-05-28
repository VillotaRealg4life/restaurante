from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'email']  # Actualizados los campos del modelo
        labels = {
            'name': 'Nombre',
            'phone': 'Teléfono',
            'email': 'Correo electrónico',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-control-lg custom-form-control', 'placeholder': 'Nombre'}),
            'phone': forms.TextInput(attrs={'class': 'form-control form-control-lg custom-form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg custom-form-control', 'placeholder': 'Correo electrónico'}),
        }
