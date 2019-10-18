from django.shortcuts import render, get_object_or_404
from .models import Cafe
# Create your views here.
def homepage(request):
    cafes = Cafe.objects
    return render(request, 'cafes/home.html', {'cafes':cafes})

def detail(request, cafe_id):
    cafe_detail = get_object_or_404(Cafe, pk=cafe_id)
    return render(request, 'cafes/details.html', {'cafe':cafe_detail})
