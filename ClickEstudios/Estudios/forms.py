from django import forms
from . import models

class Service(forms.ModelForm):
      class Meta:
            model = models.Service
            fields = ['name', 'description',  'img', 'is_active']
            widgets = {
                  'name': forms.TextInput(attrs={'class': 'form-control'}),
                  'description': forms.Textarea(attrs={'class': 'form-control'}),
                  'img': forms.FileInput(attrs={'class': 'form-control'}),
                  'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})

            }


class Plan(forms.ModelForm):
      class Meta:
            model = models.Plan
            fields = ['service', 'name', 'description', 'price', 'img', 'img_back', 'is_active']
            widgets = {
                  'service': forms.Select(attrs={'class': 'form-control'}),
                  'name': forms.TextInput(attrs={'class': 'form-control'}),
                  'description': forms.Textarea(attrs={'class': 'form-control'}),
                  'price': forms.NumberInput(attrs={'class': 'form-control'}),
                  'img': forms.FileInput(attrs={'class': 'form-control'}),
                  'img_back': forms.FileInput(attrs={'class': 'form-control'}),
                  'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})
            }




class Client(forms.ModelForm):
      class Meta:
            model = models.Client
            fields = ['name', 'last_name', 'email', 'phone', ]
            widgets = {
                  'name': forms.TextInput(attrs={'class': 'form-control'}),
                  'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                  'email': forms.EmailInput(attrs={'class': 'form-control'}),
                  'phone': forms.TextInput(attrs={'class': 'form-control'}),
            }



class Sale(forms.ModelForm):
      class Meta:
            model = models.Sale
            fields = [
                  'client', 'name_plan', 'description_plan', 'price_plan', 'is_active',
                  'mount', 'is_reserve', 'payment', 'start_proces_date', 'end_proces_date',
                  'finalize', 'date_choice', 'time', 'credit_fiscal', 'name_client', 'email_client', 'phone_client', 'is_cliente'
            ]
            widgets = {
                    'client': forms.Select(attrs={'class': 'form-control'}),
                    'name_plan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del plan'}),
                    'description_plan': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del plan'}),
                    'price_plan': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Precio del plan'}),
                    'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                    'mount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Monto'}),
                    'is_reserve': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                    'payment': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Pago'}),
                    'start_proces_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha de inicio'}),
                    'end_proces_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha de fin'}),
                    'finalize': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                    'date_choice': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'placeholder': 'Fecha de elección'}),
                    'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'placeholder': 'Hora'}),
                    'credit_fiscal': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                    'name_client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del cliente'}),
                    'email_client': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico del cliente'}),
                    'phone_client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono del cliente'}),
            }




class Adicional(forms.ModelForm):
      class Meta:
            model = models.Adicional
            fields = ['sale', 'name', 'description', 'price', ]
            widgets = {
                  'sale': forms.Select(attrs={'class': 'form-control'}),
                  'name': forms.TextInput(attrs={'class': 'form-control'}),
                  'description': forms.Textarea(attrs={'class': 'form-control'}),
                  'price': forms.NumberInput(attrs={'class': 'form-control'}),

            }


class Box(forms.ModelForm):
      class Meta:
            model = models.Box
            fields = [ 'user', 'open', 'date_close']
            widgets = {

            'user': forms.Select(attrs={'class': 'form-control'}),
            'open': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'date_close': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            }