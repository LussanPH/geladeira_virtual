from django.http import HttpResponse
from django.shortcuts import render

def teste_view(request):
    return HttpResponse("Essa rota é de teste!")

def index_view(request):
    context = {
        "nome":"Pedro"
    }
    return render(request, 'home.html', context)