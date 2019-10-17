from django.shortcuts import render
from .models import Cafe
# Create your views here.
def homepage(request):
    cafes = Cafe.objects
    return render(request, 'cafes/home.html', {'cafes':cafes})
