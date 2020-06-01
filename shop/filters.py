import django_filters
from .models import Product
from django import forms


COLOR_CHOICES = (
    ('White', 'Белый'),
    ('Black', 'Черный'),
    ('Blue', 'Синий'),
    ('Green', 'Зеленый'),
    ('Red', 'Красный'),
    ('Yellow', 'Желтый'),
    ('Orange', 'Оранжевый'),
    ('Violet', 'Фиолетовый'),
    ('Brown', 'Коричневый'),
    ('Grey', 'Серый')
)


SIZE_CHOICES = (
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL')
)


TYPE_CHOICES = (
    ('Male', 'Мужской'),
    ('Female', 'Женский')
)


class ProductFilter(django_filters.FilterSet):

    sex_type = django_filters.MultipleChoiceFilter(
        choices=TYPE_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    color = django_filters.MultipleChoiceFilter(
        choices=COLOR_CHOICES,
        widget=forms.CheckboxSelectMultiple)
    size = django_filters.MultipleChoiceFilter(
        choices=SIZE_CHOICES,
        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ('sex_type', 'color', 'size')
