from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

def home(request: WSGIRequest):
    render(request, 'intex.html')