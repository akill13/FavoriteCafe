from django.shortcuts import render
from .models import Cafe
# Create your views here.
def homepage(request):
    cafes = Cafe.objects
    return render(request, 'cafes/home.html', {'cafes':cafes})

def detail(request, cafe_name):
    print(cafe_name)
    return render(request, 'cafes/home.html')
