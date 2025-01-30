from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm
from categories.models import Category


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    ctx = {'product': product}
    return render(request, 'products/detail.html', ctx)


def product_list(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    category = request.GET.get('category')
    sort = request.GET.get('sort')
    search_query = request.GET.get('search')

    if category:
        products = products.filter(category__id=category)

    if search_query:
        products = products.filter(name__icontains=search_query)

    if sort == 'price':
        products = products.order_by('price')
    elif sort == '-price':
        products = products.order_by('-price')
    elif sort == 'name':
        products = products.order_by('name')

    ctx = {
        'products': products,
        'categories': categories,
        'category': category,
        'search': search_query,
    }
    return render(request, 'products/list.html', ctx)


def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            messages.success(request, 'Product created successfully.')
            return redirect('products:product_list')
    else:
        form = ProductForm()
    return render(request, 'products/form.html', {'form': form})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                setattr(product, key, value)
            product.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('products:product_list')
    else:
        form = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'category': product.category,
        })
    return render(request, 'products/form.html', {'form': form, 'product': product})


def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('products:product_list')
    return render(request, 'products/delete-confirm.html', {'product': product})
