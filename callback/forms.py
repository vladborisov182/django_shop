from django import forms
from django.core.validators import RegexValidator

class Callback_Form(forms.Form):
    name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'placeholder':'Имя', 'class':'form-control'}))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'type':'phone', 'class':'form-control', 'required': 'True', 'pattern': "[0-9_-]{10}", 'title': 'Пример: +380-88-888-88-88'}), validators=[RegexValidator('^((\+3)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$')])