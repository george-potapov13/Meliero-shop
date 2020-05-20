from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .filters import ProductFilter


def product_list(request, product_id=None, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    cart_product_form = CartAddProductForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    product_filter = ProductFilter(request.GET, queryset=products)
    paginator = Paginator(product_filter.qs, 12)
    page = request.GET.get('page')

    try:
        product_list = paginator.page(page)
    except PageNotAnInteger:
        product_list = paginator.page(1)
    except EmptyPage:
        product_list = paginator.page(paginator.num_pages)

    context = {
        'category': category,
        'categories': categories,
        'product_list': product_list,
        'page': page,
        'filter': product_filter,
        'form': cart_product_form
    }
    template_name = 'shop/product_list.html'
    return render(request, template_name, context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    template_name = 'shop/product_detail.html'
    return render(request, template_name, context)


'''
>>> min = Product.objects.all().aggregate(Min('price'))
>>> min_price = 0
>>> for i in min:
...     min_price += min[i]
...
>>> print(min_price)
100
'''
