from django.shortcuts import render, redirect, get_object_or_404
from orders.models import Order
from .forms import OrderForm
from django.contrib import messages


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/list.html', {'orders': orders})


def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders/detail.html', {'order': order})


def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order created successfully.')
            return redirect('orders:order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/form.html', {'form': form})


def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders:order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/form.html', {'form': form})


def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.delete()
        messages.success(request, 'Order deleted successfully.')
        return redirect('orders:order_list')