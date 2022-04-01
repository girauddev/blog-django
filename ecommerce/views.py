from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from ecommerce.models import Mouse, Display, Headphone
from ecommerce.forms import MouseForm, DisplayForm, HeadphoneForm

# Creamos las vistas de nuestra plataforma ecomerce
def inicio(request):
    return render(request, 'ecommerce/index.html')

def mouses(request):
    mouses = Mouse.objects.all()
    return render(request, 'ecommerce/mouses.html', {'mouses': mouses})

def displays(request):
    displays = Display.objects.all()
    return render(request, 'ecommerce/displays.html', {'displays': displays})

def headphones(request):
    headphones = Headphone.objects.all()
    return render(request, 'ecommerce/headphones.html', {'headphones': headphones})

#Creamos la carga de Mouses
def load_mouse(request):
    if request.method == 'POST':
        mouse_form = MouseForm(request.POST)
        if mouse_form.is_valid():
            data = mouse_form.cleaned_data
            mouse_form_new = Mouse(nombre=data['nombre'], marca=data['marca'], modelo=data['modelo'], color=data['color'], descripcion=data['descripcion'])
            # mouse_form_new = Mouse(data['nombre'], data['marca'], data['modelo'], data['color'], data['descripcion'])
            mouse_form_new.save()
        return render(request, 'ecommerce/index.html')
    else: 
        mouse_form = MouseForm()
        return render(request, 'ecommerce/load_mouse.html', {"mouse_form":mouse_form})

#Creamos la carga de Displays
def load_display(request): 
    if request.method == 'POST':
        display_form = DisplayForm(request.POST)
        if display_form.is_valid():
            data = display_form.cleaned_data
            display_form_new = Display(nombre=data['nombre'], marca=data['marca'], modelo=data['modelo'], color=data['color'], pulgadas=data['pulgadas'], resolucion=data['resolucion'], descripcion=data['descripcion'])
            display_form_new.save()
        return render(request, 'ecommerce/index.html')
    else: 
        display_form = DisplayForm()
        return render(request, 'ecommerce/load_display.html', {"display_form":display_form})

#Creamos la carga de Headphones
def load_headphone(request): 
    if request.method == 'POST':
        headphone_form = HeadphoneForm(request.POST)
        if headphone_form.is_valid():
            data = headphone_form.cleaned_data
            headphone_form_new = Headphone(nombre=data['nombre'], marca=data['marca'], modelo=data['modelo'], color=data['color'], sonido=data['sonido'], descripcion=data['descripcion'])
            headphone_form_new.save()
        return render(request, 'ecommerce/index.html')
    else: 
        headphone_form = HeadphoneForm()
        return render(request, 'ecommerce/load_headphone.html', {"headphone_form":headphone_form})

#Creamos la busqueda de Mouse
def busquedaMouse(request):
    data = request.GET.get('nombre', '')
    error = ''
    if data:
        try:
            mouse = Mouse.objects.get(nombre = data)
            return render(request, 'ecommerce/busquedaMouse.html', {'mouse': mouse, 'id': data})
        
        except Exception as exc:
            print(exc)
            error = 'No existe ese mouse'
            
    return render(request, 'ecommerce/busquedaMouse.html', {'error': error})