from unicodedata import name
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', name='index')

def contact(request):
    return render(request, 'contact.html', name='contact')

def about(request):
    return render(request, 'about.html', name='about')