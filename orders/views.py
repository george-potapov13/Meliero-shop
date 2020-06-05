from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from .tasks import order_created
from django.contrib import messages


def order_create(request):
    cart = Cart(request)
    if cart.__len__() > 0:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                if cart.coupon:
                    order.coupon = cart.coupon
                    order.discount = cart.coupon.discount
                order.save()
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'])
                    # clear the cart
                    cart.clear()
                    # launch asynchronous task
                    order_created.delay(order.id)
                    messages.success(
                        request, 'Ваш заказ успешно зарегистрирован. Мы отправили вам письмо с номером заказа на адрес почты который вы указали при заполнении формы.')
                    return redirect("shop:product_list")
        else:
            form = OrderCreateForm()
        return render(request,
                      'orders/order_create.html',
                      {'cart': cart, 'form': form})
    else:
        messages.success(
                        request, 'Ваша корзина пуста. Для перехода по ссылке необходимо добавить товары в корзину и подтвердить заказ.')
        return redirect("shop:product_list")
