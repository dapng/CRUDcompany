from django.db import models
from .models import Employ
from django.forms import ModelForm, fields, widgets, TextInput, DateTimeInput, Textarea, NumberInput


class EmployForm(ModelForm):
    class Meta:
        model = Employ
        fields = ['title', 'first_name', 'last_name', 'staff_name', 'age', 'staff_exp', 'wages', 'education', 'duties']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок сотрудника для списка'
            }),
            "first_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            "last_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            "staff_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Должность'
            }),
            "age": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Возраст'
            }),
            "staff_exp": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стаж'
            }),
            "wages": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ЗП'
            }),
            "education": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Образование'
            }),
            "duties": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Обязанности'
            }),
        }