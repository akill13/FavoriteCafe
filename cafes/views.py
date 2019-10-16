from django.shortcuts import render

# Create your views here.
def akill(request):
    return render(request, 'cafes/home.html')
