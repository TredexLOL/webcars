from django.db import models

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('механика', 'Механическая'),
        ('автомат', 'Автоматическая'),
        ('АКПП','АКПП'),
        ('Робот','Робот'),
        ('Вариатор','Вариатор'),
        # Добавьте другие типы трансмиссии, если нужно
    ]
    FUEL_CHOICE = [
        ('Дизель','Дизель'),
        ('Бензин','Бензин'),
        ('Электро','Электро'),
        ('Гибрид','Гибрид'),
        ('ГБО','ГБО'),
    ]

    mark = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=30)
    transmission = models.CharField(max_length=30, choices=TRANSMISSION_CHOICES)
    mileage = models.IntegerField()
    fuel = models.CharField(max_length=30, choices=FUEL_CHOICE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(upload_to='car_images', blank=True, null=True)


    def __str__(self):
        return f"{self.mark} {self.model} ({self.year})"