from django import forms
from .models import *
from django.core.exceptions import ValidationError

class FormPaciente(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'apellido': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'patologias': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
            'active': forms.HiddenInput
        }

class FormConsulta(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'readonly': True
                },
            ),
            'hora': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'modalidad': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'active': forms.HiddenInput
        }

    def clean_tipo(self):
            data = self.cleaned_data["tipo"]
            paciente = self.cleaned_data["paciente"]
            if data == 'CONTROL' and not Consulta.objects.filter(paciente=paciente):
                raise ValidationError("No se registra ingreso para este paciente")
            return data

class FormConsultaPaciente(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date',
                    'readonly': True
                },
            ),
            'hora': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'readonly': True
                }
            ),
            'tipo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'estado': forms.HiddenInput,
            'modalidad': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'active': forms.HiddenInput
        }

    def clean_tipo(self):
            data = self.cleaned_data["tipo"]
            paciente = self.cleaned_data["paciente"]
            if data == 'CONTROL' and not Consulta.objects.filter(paciente=paciente):
                raise ValidationError("No se registra ingreso para este paciente")
            return data
    

class FormDatosPaciente(forms.ModelForm):
    class Meta:
        model = DatosPaciente
        fields = '__all__'
        widgets = {
            'paciente': forms.HiddenInput,
            'diagnostico': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'peso': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onkeyup': 'setIMC("id_peso", "id_talla", "id_imc");'
                }
            ),
            'talla': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'onkeyup': 'setIMC("id_peso", "id_talla", "id_imc");'
                }
            ),
            'imc': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'disabled': True
                }
            ),
            'active': forms.HiddenInput
        }