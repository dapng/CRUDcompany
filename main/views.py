from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/main.html')


def products(request):
    return render(request, 'main/products.html')


def about(request):
    return render(request, 'main/about.html')


def ceo(request):
    return render(request, 'main/ceo.html')


def cvo(request):
    return render(request, 'main/cvo.html')


def doc(request):
    return render(request, 'main/doc.html')


def employees(request):
    return render(request, 'main/employees.html')


def contact(request):
    return render(request, 'main/contact.html')