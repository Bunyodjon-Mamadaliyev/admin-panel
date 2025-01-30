from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category
from .forms import CategoryForm
from products.models import Product
from orders.models import Order
from django.db.models import Sum


def dashboard(request):
    total_price = Product.objects.aggregate(Sum('price'))['price__sum']
    total_categories = Category.objects.count()
    total_orders = Order.objects.annotate(total_quantity=Sum('items__quantity')).aggregate(total=Sum('total_quantity'))[
        'total']
    recent_products = Product.objects.all().order_by('-created_at')[:9]
    category_names = [category.name for category in Category.objects.all()]
    category_product_counts = [category.products.count() for category in Category.objects.all()]
    max_products = 1000
    total_price = total_price or 0
    max_products = max_products or 1
    product_scale_percentage = min((total_price / max_products) * 100, 100)
    ctx = {
        'total_price': total_price,
        'total_categories': total_categories,
        'total_orders': total_orders,
        'recent_products': recent_products,
        'category_names': category_names,
        'category_product_counts': category_product_counts,
        'product_scale_percentage': product_scale_percentage,
    }
    return render(request, 'index.html', ctx)


def category_detail(request, year, month, day, slug):
    category = get_object_or_404(
        Category,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )
    ctx = {'category': category}
    return render(request, 'categories/detail.html', ctx)


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/list.html', {'categories': categories})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            messages.success(request, 'Category created successfully.')
            return redirect('categories:category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/form.html', {'form': form})


def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            for key, value in form.cleaned_data.items():
                setattr(category, key, value)
            category.save()
            messages.success(request, 'Category updated successfully.')
            return redirect('categories:category_list')
    else:
        form = CategoryForm(initial={
            'name': category.name,
            'description': category.description,
        })
    return render(request, 'categories/form.html', {'form': form, 'category': category})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('categories:category_list')
    return render(request, 'categories/delete-confirm.html', {'category': category})