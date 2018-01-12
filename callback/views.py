from django.shortcuts import render, redirect
from .forms import Callback_Form
from django.core.mail import send_mail, get_connection

def CallbackForm(request):
    if request.method == 'POST':
        form = Callback_Form(request.POST)
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        if form.is_valid():
            mail_host = 'smtp.mailtrap.io'
            recipients = ['blinkvlad182@gmail.com']
            message = '''
                На вашем сайте появилась новая заявка на звонок! Вот данные, предоставленные пользователем:
                Имя:{0}
                Телефон: {1}'''.format(name, phone)
            subject = 'Заявка на звонок'
            send_mail(subject, message, mail_host, recipients, fail_silently=False)
            return render(request, 'callback/thanks.html')
        else:
            return render(request, 'callback/error.html')

    return render(request, 'callback/callbackform.html', locals())
