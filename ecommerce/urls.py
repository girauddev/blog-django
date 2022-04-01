from django.urls import path
from ecommerce.views import *

#Cargamos los paths a nuestras urls

urlpatterns = [
    path('', inicio, name= 'Ecommerce Barats'),
    path('mouses/', mouses, name= 'Mouses'),
    path('displays/', displays, name= 'Displays'),
    path('headphones/', headphones, name= 'Headphones'),
    path('load_mouse/', load_mouse, name ='load_mouse'),
    path('load_display/', load_display, name ='load_display'),
    path('load_headphone/', load_headphone, name ='load_headphone'),
    path('busquedaMouse/', busquedaMouse, name ='Busqueda Mouse')
]