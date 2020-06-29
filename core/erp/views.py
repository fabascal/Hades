from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from core.erp.models import Category, Product


def myfirstview(request):
    data = {
        'categories' : Category.objects.all(),
    }
    return render(request,'index.html',data)
    #funcion para regresar un httpresponse
    # return HttpResponse('Hola esta es mi primer URL creada.')
    #funcion para retornar un Json
    # return JsonResponse(data)

def mysecondview(request):
    data = {
        'products' : Product.objects.all(),
    }
    return render(request,'second.html',data)