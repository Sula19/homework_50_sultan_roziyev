from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from webapp.bd import DataBase


def view_cat(request: WSGIRequest):
    action = request.POST.get('action')
    DataBase.action(action)
    DataBase.name = request.POST.get('name', DataBase.name)
    context = {
        'name': DataBase.name,
        'age': DataBase.age,
        'happiness': DataBase.happiness,
        'satiety': DataBase.satiety,
        'energy': DataBase.energy,
    }
    return render(request, 'cat_stats.html', context=context)
