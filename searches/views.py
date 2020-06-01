from django.shortcuts import render
from shop.models import Product, Category
from django.views.generic import ListView
from django.db.models import Q


class SearchView(ListView):
    model = Product
    template_name = 'searches/search_results.html'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q')
        products = Product.objects.filter(available=True)
        object_list = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        return object_list
