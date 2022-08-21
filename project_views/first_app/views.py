from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def simple_view(request):
    return HttpResponse('A simple view')