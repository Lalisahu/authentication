from django.shortcuts import render


def app(request):
    
    return render(request, 'index.html')

# Create your views here.
