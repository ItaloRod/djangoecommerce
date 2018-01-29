#coding=utf-8
from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views import generic

class productListView(generic.ListView):
    
    #Lista modelos do banco de dados baseado em um queryset.

    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 3

product_list = productListView.as_view()

class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'
    paginate_by = 3
    def get_queryset(self):
        return Product.objects.filter(category__slug = self.kwargs['slug'])
       # category = get_object_or_404(Category, slug = self.kwargs['slug'])
       # return Product.objects.filter(category = category)

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

category = CategoryListView.as_view()

class productView(generic.ListView):

    template_name = 'catalog/product.html'
    context_object_name = 'product'
    

    def get_queryset(self):
        return get_object_or_404(Product, slug = self.kwargs['slug'])
    
product = productView.as_view()