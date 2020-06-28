from django.db import models
from datetime import datetime

# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=150,verbose_name='Nombres', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        db_table = 'type'
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombres')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'category'
        ordering = ['id']


class Employee(models.Model):
    categ = models.ManyToManyField(Category)
    #ForeignKey se utiliza para relacionar con otra tabla
    type = models.ForeignKey(Type, on_delete=models.PROTECT)
    #verbose_name se usa para mostrar las varibles en las vistas
    names = models.CharField(max_length=150,verbose_name='Nombres')
    ine = models.CharField(max_length=10, unique=True,verbose_name='INE')
    date_joined = models.DateTimeField(default=datetime.now,verbose_name='Fecha de registro')
    #auto_now en true sirve para que cuando se cree el registro obtiene la fecha actual
    date_creation = models.DateTimeField(auto_now=True)
    #auto_now_add sirve para que cada que se actualice un campo se registre la fecha actual
    date_update = models.DateTimeField(auto_now_add=True)
    age = models.PositiveIntegerField(default=0)
    salary = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    state = models.BooleanField(default=True)
    #gender = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', null=True, blank=True)
    cvitae = models.FileField(upload_to='cvitae/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.names

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        db_table = 'empleado'
        ordering = ['id']
