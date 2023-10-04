from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_apellido', 'telefono', 'email', 'tipo_servicio', 'consulta']

        