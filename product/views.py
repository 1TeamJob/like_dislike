from django.shortcuts import render, redirect
from .models import Product
from django.urls import reverse
from .forms import ProductForm
from django.contrib.auth.decorators import login_required


def product_list(request):
    products = Product.objects.all()
    
    
    context = {'products': products}
    return render(request, 'product/product_list.html', context)



def product_details(request, slug):
    product = Product.objects.get(slug=slug)
    
    
    context = {'product': product}
    return render(request, 'product/product_details.html', context)    



def like_dislike(request, slug):
    product = Product.objects.get(slug=slug)
    
    
    if request.user in product.like.all():
        product.like.remove(request.user)
        
    
    else:
        product.like.add(request.user)
    
    
    context = {'slug': product.slug}
    return redirect(reverse('products:product_details', kwargs=context))



@login_required
def add_products(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.owner = request.user
            my_form.save()
            return redirect(reverse('products:product_list'))
    
    
    else:
        form = ProductForm
    
    
    context = {'form': form}
    return render(request, 'product/add_products.html', context)


@login_required
def edit_product(request, slug):
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('products:product_list'))
    
    
    else:
        form = ProductForm(instance=product)
    
    
    context = {'form': form}
    return render(request, 'product/edit_product.html', context)



