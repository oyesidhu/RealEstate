from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'index.html')


def contactus(request):
    return render(request, 'contactus.html')


def search_property(request):
    return render(request, 'search_property.html')


def advertise_property(request):
    return render(request, 'advertise_property.html')


def register(request):
    return render(request, 'sign_in.html')


def about(request):
    return render(request, 'about.html')
