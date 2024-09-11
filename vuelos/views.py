
from django.shortcuts import render, redirect
from .forms import FlightForm
from .models import Flight
from django.db.models import Avg

def home(request):
    return render(request, 'vuelos/home.html')

def registrar_vuelo(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_vuelos')
    else:
        form = FlightForm()
    return render(request, 'vuelos/registrar_vuelo.html', {'form': form})



def listar_vuelos(request):
    vuelos = Flight.objects.order_by('price')
    return render(request, 'vuelos/listar_vuelos.html', {'vuelos': vuelos})

def estadisticas_vuelos(request):
    vuelos_nacionales = Flight.objects.filter(type='Nacional').count()
    vuelos_internacionales = Flight.objects.filter(type='Internacional').count()
    promedio_precio_nacional = Flight.objects.filter(type='Nacional').aggregate(Avg('price'))['price__avg'] or 0
    return render(request, 'vuelos/estadisticas_vuelos.html', {
        'vuelos_nacionales': vuelos_nacionales,
        'vuelos_internacionales': vuelos_internacionales,
        'promedio_precio_nacional': promedio_precio_nacional
    })