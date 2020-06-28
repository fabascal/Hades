from config.wsgi import *
from django.test import TestCase
from core.erp.models import Type

# Create your tests here.

#listar (Select * tabla)

# query = Type.objects.all()
# print (query)


#Insert
# type = Type()
# type.name = 'Accionista'
# type.save()

#Edicion

# t = Type.objects.get(pk=1)
# t.name='Accionistas'
# t.save()
# t = Type.objects.get(pk=1)
# print (t.name)
#
# #Eliminar
#
# t = Type.objects.get(pk=1)
# t.delete()


try :
    #name_contains es para una consulta like y es case sensitive
    obj = Type.objects.filter(name__contains='pre')
    #name_contains es para una consulta like y no es case sensitive
    obj = Type.objects.filter(name__icontains='pre')
    #name_startwith es para una consulta like que epieze como
    obj = Type.objects.filter(name__startwith='pre')
    #name_endwith es para una consulta like que termine como
    obj = Type.objects.filter(name__startwith='pre')
    #name_in es para una consulta like con varias opciones de busqueda
    obj = Type.objects.filter(name__in=['pre','sidente'])
    #is_null es para si el registro es null
    obj = Type.objects.filter(is_null=True)
    #.count es para contar el numero de registros
    obj = Type.objects.filter(name__in=['pre','sidente']).count()
    #exclude es para excluir algun registro
    obj = Type.objects.filter(name__in=['pre','sidente']).exclude(id=5)

    if obj:
        print(obj)
    else:
        print("not found")
except Exception as e:
    print(e)
