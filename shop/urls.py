from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('shop/', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'),
    path('<int:id>/<str:slug>/', views.product_detail, name='product_detail')
]
