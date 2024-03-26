from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """ Busca o arquivo dentro da pasta templates """
    return render(request, 'recipes/pages/home.html')
