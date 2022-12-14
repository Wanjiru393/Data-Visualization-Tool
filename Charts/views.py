from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm,ProductForm, OrderForm
from .models import Product,Order


# Create your views here.
@login_required(login_url='login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)
#Read Product
@login_required(login_url='login')
def product(request):
    items = Product.objects.all()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form':form,
    }
    return render(request, 'dashboard/product.html', context)


#Delete Product
@login_required(login_url='login')
def product_delete(request, pk):
    item = Product.objects.filter(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('product')
    return render(request, 'dashboard/product_delete.html')


#Edit Product
@login_required(login_url='login')
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_edit.html', context)



@login_required(login_url='login')
def user(request):
    customers = User.objects.all()  #Error(Admin is displayed on repeat)
    context={
        'customers':customers
    }
    return render(request, 'dashboard/user.html', context)

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateUserForm()
    context = {
        'form':form,
    }
    return render(request, 'user/register.html',context)

@login_required(login_url='login')
def order(request):
    orders = Order.objects.all()
    context = {
        'orders':orders,
    }
    return render(request, 'dashboard/order.html',context)

def profile(request):
    return render(request, 'user/profile.html')