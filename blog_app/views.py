from django.shortcuts import get_object_or_404, redirect, render
from .models import Category, Product

# Create your views here.

def home(request):
    context = {
        'total_categories': Category.objects.filter(is_deleted=False).count(),
        'total_products': Product.objects.filter(is_deleted=False).count(),
        'products_in_trash': Product.objects.filter(is_deleted=True).count(),
        'categories_in_trash': Category.objects.filter(is_deleted=True).count(),
    }
    return render(request, 'home.html', context)

# ==================== Category ====================

def category_list(request):
    data = Category.objects.filter(is_deleted=False).order_by('id')
    return render(request, 'category.html', {'data': data})

def deleted_category_list(request):
    data = Category.objects.filter(is_deleted=True).order_by('id')
    return render(request, 'deleted_category.html', {'data': data})

def add_category(request):
    return render(request, 'add_category.html')

def save_category(request):
    try:
        if request.method != 'POST':
            return redirect('add_category')
        else:
            txtname = request.POST.get('txt_name')
            new_category = Category(name=txtname)
            new_category.save()
            return redirect('category_list')
    except Exception as ex:
        return redirect('add_category')

def edit_category(request, id):
    try:
        category = Category.objects.get(id=id)
        context = {
            'category': category
        }
        return render(request, 'edit_category.html', context)
    except Exception as ex:
        return redirect('category_list')

def update_category(request):
    try:
        cat_id = request.POST.get('txt_id')
        cat_name = request.POST.get('txt_name')
        category = Category.objects.get(id=cat_id)
        if not category:
            return redirect('category_list')
        category.name = cat_name
        category.save()
        return redirect('category_list')
    except Exception as ex:
        return redirect('category_list')

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.is_deleted = True
    category.save()
    return redirect('category_list')

def restore_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.is_deleted = False
    category.save()
    return redirect('deleted_category_list')

def permanent_delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    if Product.objects.filter(CategoryId=category).exists():
        return redirect('deleted_category_list')
    category.delete()
    return redirect('deleted_category_list')

# ==================== Product ====================

def product_list(request):
    data = Product.objects.select_related('CategoryId').filter(is_deleted=False).order_by('ProductId')
    return render(request, 'product.html', {'data': data})

def deleted_product_list(request):
    data = Product.objects.select_related('CategoryId').filter(is_deleted=True).order_by('ProductId')
    return render(request, 'deleted_product.html', {'data': data})

def add_product(request):
    categories = Category.objects.all()
    return render(request, 'add_product.html', {'categories': categories})

def save_product(request):
    try:
        if request.method != 'POST':
            return redirect('add_product')
        else:
            product_name = request.POST.get('txt_product_name')
            barcode     = request.POST.get('txt_barcode')
            price       = request.POST.get('txt_price')
            cost        = request.POST.get('txt_cost')
            qty         = request.POST.get('txt_qty')
            unit        = request.POST.get('txt_unit')
            description = request.POST.get('txt_description')
            category_id = request.POST.get('txt_category_id')

            category = Category.objects.get(id=category_id)
            new_product = Product(
                ProductName  = product_name,
                Barcode      = barcode,
                Price        = price,
                Cost         = cost,
                Qty          = qty,
                Unit         = unit,
                Description  = description,
                CategoryId   = category
            )
            new_product.save()
            return redirect('product_list')
    except Exception as ex:
        return redirect('add_product')

def edit_product(request, id):
    try:
        product    = Product.objects.get(ProductId=id)
        categories = Category.objects.all()
        context = {
            'product'   : product,
            'categories': categories
        }
        return render(request, 'edit_product.html', context)
    except Exception as ex:
        return redirect('product_list')

def update_product(request):
    try:
        product_id  = request.POST.get('txt_id')
        product_name = request.POST.get('txt_product_name')
        barcode     = request.POST.get('txt_barcode')
        price       = request.POST.get('txt_price')
        cost        = request.POST.get('txt_cost')
        qty         = request.POST.get('txt_qty')
        unit        = request.POST.get('txt_unit')
        description = request.POST.get('txt_description')
        category_id = request.POST.get('txt_category_id')

        product = Product.objects.get(ProductId=product_id)
        if not product:
            return redirect('product_list')

        category = Category.objects.get(id=category_id)
        product.ProductName = product_name
        product.Barcode     = barcode
        product.Price       = price
        product.Cost        = cost
        product.Qty         = qty
        product.Unit        = unit
        product.Description = description
        product.CategoryId  = category
        product.save()
        return redirect('product_list')
    except Exception as ex:
        return redirect('product_list')

def delete_product(request, id):
    product = get_object_or_404(Product, ProductId=id)
    product.is_deleted = True
    product.save()
    return redirect('product_list')

def restore_product(request, id):
    product = get_object_or_404(Product, ProductId=id)
    product.is_deleted = False
    product.save()
    return redirect('deleted_product_list')

def permanent_delete_product(request, id):
    product = get_object_or_404(Product, ProductId=id)
    product.delete()
    return redirect('deleted_product_list')