from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('contact/', contact, name='contact'),
    path('contact_view/', contact_view, name='contact_view'),
    path('catalog/', catalog, name='catal'),
    path('descript/<int:car_id>', description, name='description'),
    path('send_email/', send_email, name='send_email')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
