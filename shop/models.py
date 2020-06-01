from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100,
                            db_index=True)
    slug = models.SlugField(max_length=100,
                            unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


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
    ('Female', 'Женский'),
)


class Product(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True)
    slug = models.SlugField(max_length=200,
                            db_index=True)
    description = models.TextField()
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    color = models.CharField(max_length=10, choices=COLOR_CHOICES)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    sex_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    image = models.ImageField(upload_to="images")
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
