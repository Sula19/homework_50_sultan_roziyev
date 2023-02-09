from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest


def add_view(request: WSGIRequest):
     return render(request, 'add_cat.html')
