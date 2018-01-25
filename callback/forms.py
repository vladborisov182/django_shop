from django import forms
from django.core.mail import send_mail
from django.core.validators import RegexValidator


class CallbackForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'placeholder':'Имя', 'class':'form-control', 'title': 'Ваше имя'}))
    phone = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'placeholder':'Телефон', 'type':'phone', 'class':'form-control', 'required': 'True', 'title': 'Пример: 80XXYYYYYYY'}))

    def send(name, phone):
            mail_host = 'smtp.mailtrap.io'
            recipients = ['blinkvlad182@gmail.com']
            message = '''
                На вашем сайте появилась новая заявка на звонок! Вот данные, предоставленные пользователем:
                Имя:{0}
                Телефон: {1}'''.format(name, phone)
            subject = 'Заявка на звонок'
            send_mail(subject, message, mail_host, recipients, fail_silently=False)
