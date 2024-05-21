from django.shortcuts import render

from mysite import settings
from .models import Car
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html', {'title' : 'Main'})

def catalog(request):
    objects=Car.objects.all()
    return render(request, 'cars.html', {'cars' : objects})

def contact(request):
    return render(request, 'contact.html', {'title' : 'Contact'})

def description(request, car_id):
    obj = Car.objects.get(id=car_id)
    return render(request, 'description.html', {'car' : obj})

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        send_mail(
            'Запрос информации',
            f'Имя: {name}\nEmail: {email}\nСообщение: {message}',
            'your-email@example.com',  # Отправитель
            ['your-email@example.com'],  # Список получателей
        )

    return render(request, '/')  # Замените 'your_template.html'
def send_email(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Тема письма
        subject = f'New Contact from {first_name} {last_name}'

        # Сообщение письма
        full_message = f'Received message below from {email}\n\n{message}'

        # Отправка письма
        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['sonicaleksej339@gmail.com'], # Замените на адрес, на который должно приходить письмо
            fail_silently=False,
        )
        return HttpResponse("Сообщение успешно отправлено")
    else:
        return HttpResponse("Ошибка отправки сообщения", status=400)