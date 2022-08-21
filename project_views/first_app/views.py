from django.http import HttpResponse
from django.shortcuts import render

articles = {
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

# Create your views here.
def news_view(request, topic):
    return HttpResponse(articles[topic])

def add_view(request, num1, num2):
    result = num1 + num2
    return HttpResponse(str(result))