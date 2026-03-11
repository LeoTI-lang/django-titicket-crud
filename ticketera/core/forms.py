from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Productora, Evento, Ubicacion, Ticket, Cliente

class ProductoraForm(forms.ModelForm):
    class Meta:
        model = Productora
        fields = '__all__'

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = '__all__'

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = '__all__'

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

class ClienteRegistroForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = [
                'username',
                'first_name', 
                'last_name', 
                'email', 
                'rut', 
                'telefono', 
                'comuna', 
                'password1', 
                'password2'
            ]