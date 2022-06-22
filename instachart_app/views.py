from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'instachart_proj/login.html')

def home(request):
    return render(request, 'instachart_proj/home.html')
