from django import forms
from .models import Trainer, Pokemon

class PokemonForm(forms.ModelForm): 
    class Meta:
        model = Pokemon
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'type': 'Tipo',
            'weight': 'Peso (kg)',
            'height': 'Altura (cm)',
            'picture': 'Imagen',
            'trainer': 'Entrenador',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'trainer': forms.Select(attrs={'class': 'form-control'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'
        labels = {
            'name': 'Nombre',
            'age': 'Edad',
            'level': 'Nivel',
            'birthday': 'Fecha de Nacimiento',
            'picture': 'Fotografía',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'level': forms.NumberInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'
            }),
            'picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }