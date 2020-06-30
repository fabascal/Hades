from django.shortcuts import render
from django.views.generic import ListView

from core.erp.models import Category


def category_list(request):
    data = {
        'title' : 'Listado de categorias.',
        'categories' : Category.objects.all()
    }
    return render(request, 'category/list.html', data)

class CategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'

    def get_queryset(self):
        return Category.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de categorias.'
        return context