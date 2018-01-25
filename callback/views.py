from callback.forms import CallbackForm
from django.shortcuts import render


def call_back(request):
    form = CallbackForm()
    if request.method == 'POST':
        form = CallbackForm(request.POST)
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        if form.is_valid():
            CallbackForm.send(name, phone)
            return render(request, 'callback/thanks.html')

    return render(request, 'callback/callbackform.html', {
        'form' : form,
})
