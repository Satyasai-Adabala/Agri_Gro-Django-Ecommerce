from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.db.models import Q
from django.urls import reverse_lazy

from .models import Product, Category, Cart, CartItem
from .forms import RegisterForm
from django.db import IntegrityError

def home(request):
    featured = Product.objects.select_related('category').order_by('-created_at')[:8]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'featured': featured,
        'categories': categories,
    })


def about(request):
    return render(request, 'store/about.html')


def product_list(request):
    products = Product.objects.select_related('category').all()
    query = request.GET.get('q', '').strip()
    category_slug = request.GET.get('category', '').strip()

    if query:
        products = products.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    if category_slug:
        products = products.filter(category__slug=category_slug)

    categories = Category.objects.all()
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
        'query': query,
        'selected_category': category_slug,
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related': related,
    })


class AgriLoginView(LoginView):
    template_name = 'store/login.html'
    redirect_authenticated_user = True


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Cart.objects.get_or_create(user=user)
            auth_login(request, user)
            messages.success(request, 'Welcome to Agri Gro! Account created successfully.')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})


@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    return render(request, 'store/cart.html', {'cart': cart})


@login_required
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f'{product.name} added to cart!')
    return redirect(request.META.get('HTTP_REFERER', 'product_list'))


@login_required
def remove_from_cart(request, pk):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    CartItem.objects.filter(cart=cart, product_id=pk).delete()
    messages.info(request, 'Item removed from cart.')
    return redirect('cart')


@login_required
def update_cart_item(request, pk):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    item = get_object_or_404(CartItem, cart=cart, product_id=pk)
    action = request.POST.get('action')
    if action == 'increase':
        item.quantity += 1
        item.save()
    elif action == 'decrease':
        item.quantity -= 1
        if item.quantity <= 0:
            item.delete()
        else:
            item.save()
    return redirect('cart')
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
            except IntegrityError:
                form.add_error('username', 'This username was just taken. Please choose another.')
            else:
                Cart.objects.get_or_create(user=user)
                auth_login(request, user)
                messages.success(request, 'Welcome to Agri Gro! Account created successfully.')
                return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'store/register.html', {'form': form})