

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product , Category
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required
@login_required
@login_required
def product_list(request):
    # 1) fetch all categories for the dropdown
    categories = Category.objects.all()

    # 2) read the selected category from the query string
    selected = request.GET.get('category', '')

    # 3) filter products if a category is selected, else show all
    if selected:
        products = Product.objects.filter(category_id=selected)
    else:
        products = Product.objects.all()

    # 4) render with extra context
    return render(request, 'stock/product_list.html', {
        'products': products,
        'categories': categories,
        'selected': selected,
    })
@login_required
def product_create(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        # grab the category if one was chosen
        cat_id = request.POST.get('category')  
        category = Category.objects.get(id=cat_id) if cat_id else None

        Product.objects.create(
            name=request.POST['name'],
            description=request.POST['description'],
            price=request.POST['price'],
            quantity=request.POST['quantity'],
            category=category,
        )
        return redirect('product-list')

    return render(request, 'stock/product_form.html', {
        'categories': categories
    })

@login_required
def product_update(request, pk):
    product    = get_object_or_404(Product, pk=pk)
    categories = Category.objects.all()
    if request.method == 'POST':
        prod = product
        prod.name        = request.POST['name']
        prod.description = request.POST['description']
        prod.price       = request.POST['price']
        prod.quantity    = int(request.POST['quantity'])
        
        cat_id = request.POST.get('category')
        prod.category = Category.objects.get(id=cat_id) if cat_id else None

        prod.save()
        return redirect('product-list')

    return render(request, 'stock/product_form.html', {
        'product':    product,
        'categories': categories,
    })
@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('product_list')
@login_required
def inventory_dashboard(request):
    # 1) Count all products
    total_products = Product.objects.count()

    # 2) Calculate total inventory value
    total_value = Product.objects.aggregate(
        total=Sum(F('price') * F('quantity'))
    )['total'] or 0

    # 3) Fetch all products and low-stock subset
    products = Product.objects.all()
    low_stock = products.filter(quantity__lt=5)

    # 4) Pass all three into the template
    return render(request, 'stock/dashboard.html', {
        'total_products': total_products,
        'total_value': total_value,
        'low_stock': low_stock,
    })
