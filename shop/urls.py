from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'shop'
urlpatterns = [
    path('shop/', views.product_list, name='product_list'),
    path('home/', views.home_page, name='home_page'),
    path('shop/<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('shop/product/<int:id>/<str:slug>/',
         views.product_detail, name='product_detail')
]

urlpatterns += [
    path('', RedirectView.as_view(url='/shop/', permanent=True)),
]
