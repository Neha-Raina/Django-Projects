from django.shortcuts import render
import pandas

# Create your views here.

def home(request):
    return render(request, 'home.html', {})
