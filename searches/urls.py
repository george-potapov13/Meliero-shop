from django.urls import path
from . import views


app_name = 'searches'
urlpatterns = [
    path('', views.SearchView.as_view(), name='search'),
]
