from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation

def home(request):
    reservations = Reservation.objects.all()
    return render(request, 'index.html', {'reservations': reservations})

def create_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio después de guardar la reserva
    else:
        form = ReservationForm()
    return render(request, 'index.html', {'reservation_form': form})
