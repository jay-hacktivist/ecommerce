from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

class ProductFeaturedListView(ListView):
    template_name = "products/product_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductFeaturedDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/featured-product_detail.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()

class ProductListView(ListView):
    # queryset = Product.objects.all()
    template_name = "products/product_list.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/product_list.html", context)


class ProductDetailView(DetailView):
    # queryset = Product.objects.all()
    template_name = "products/product_detail.html"
    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(
            *args, **kwargs)
        print(context)
        # context['abc'] = 123
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        if instance == None:
            raise Http404("Product doesn't exist.")
        return instance

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     pk = self.kwargs.get('pk')
    #     return Product.objects.filter(pk=pk)


def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = Product.objects.all(pk=pk)
    # instance = get_object_or_404(Product, pk=pk)

    # try:
    #     instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    #     print("No product here!")
    #     raise Http404("Product doesn't exist.")
    # except:
    #     print("huh?")

    # qs = Product.objects.filter(id=pk)
    # if qs.exists() and qs.count() ==1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product doesn't exist.")

    instance = Product.objects.get_by_id(pk)
    if instance == None:
        raise Http404("Product doesn't exist.")
    context = {
        'object': instance
    }
    return render(request, "products/product_detail.html", context)
