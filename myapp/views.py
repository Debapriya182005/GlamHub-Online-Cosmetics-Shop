import razorpay
import re
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import CustRegFrm, CustLogFrm, MyChngFrm, PwdChng
from .models import Item, Category, CartItem, Order, WishlistItem

def parse_price(price_str):
    """Robustly extract the numeric price from a string like '7100/-' or '₹1,500'."""
    try:
        # Remove anything that isn't a digit or a decimal point
        numeric_part = re.sub(r'[^\d.]', '', str(price_str))
        if '.' in numeric_part:
            return float(numeric_part)
        return int(numeric_part) if numeric_part else 0
    except (ValueError, TypeError):
        return 0

# Create your views here.

def home(request):
    # Fetch all categories
    categories = Category.objects.all()
    
    # Fetch specific collections
    # Using order_by('-id') ensures the latest items (the ones we just added) appear first
    featured_items = Item.objects.all().order_by('-id')[:8]
    bestsellers = Item.objects.filter(is_bestseller=True).order_by('-id')[:4]
    new_arrivals = Item.objects.filter(is_new=True).order_by('-id')[:4]
    top_rated = Item.objects.filter(is_top_rated=True).order_by('-id')[:4]
    
    # Placeholder images for categories
    cat_images = {
        "Skin Care": "https://images.unsplash.com/photo-1556228720-195a672e8a03?q=80&w=400&auto=format&fit=crop",
        "Makeup": "https://images.unsplash.com/photo-1522338223662-42664741344c?q=80&w=400&auto=format&fit=crop",
        "Hair Care": "https://images.unsplash.com/photo-1527799822344-42ad7c28274a?q=80&w=400&auto=format&fit=crop",
        "Fragrances": "https://images.unsplash.com/photo-1541643600914-78b084683601?q=80&w=400&auto=format&fit=crop",
        "Body Care": "https://images.unsplash.com/photo-1552046122-03184de85e08?q=80&w=400&auto=format&fit=crop",
        "Eye Care": "https://images.unsplash.com/photo-1512496015851-a90fb38ba796?q=80&w=400&auto=format&fit=crop",
        "Sun Care": "https://images.unsplash.com/photo-1501503069356-3c6b82a17d89?q=80&w=400&auto=format&fit=crop"
    }
    
    for cat in categories:
        if not cat.image:
            cat.placeholder_image = cat_images.get(cat.cat_name, "https://images.unsplash.com/photo-1522335789203-aabd1fc54bc9?q=80&w=400&auto=format&fit=crop")
        
    context = {
        'featured_items': featured_items,
        'categories': categories[:6],
        'bestsellers': bestsellers,
        'new_arrivals': new_arrivals,
        'top_rated': top_rated
    }
    
    return render(request, 'home.html', context)

def shop(request):
    allcate = Category.objects.all()
    allitem = Item.objects.all()
    return render(request, 'shop.html', {'allitem': allitem, 'allcate': allcate})

def shopCate(request, id):
    allcate = Category.objects.all()
    allitem = Item.objects.filter(category=id)
    return render(request, 'shop.html', {'allitem': allitem, 'allcate': allcate})

def about(request):
    return render(request, 'about-us.html')

def contact(request):
    return render(request, 'contact.html')

def custLog(request):
    if request.method == "POST":
        form = CustLogFrm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user.first_name or user.username}!")
                return redirect('/')
    else:
        form = CustLogFrm()
    return render(request, 'login.html', {'form': form})

def custReg(request):
    if request.method == "POST":
        form = CustRegFrm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Your registration is successful. Please Login.')
                return redirect('/login')
            except Exception:
                messages.error(request, 'Your registration is not successful')
    else:
        form = CustRegFrm()
    return render(request, 'custreg.html', {'form': form})

def custLogout(request):
    logout(request)
    return redirect('/login')

def add_to_cart(request, id):
    if request.user.is_authenticated:
        product = get_object_or_404(Item, id=id)
        cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f"{product.name} added to cart.")
        return redirect('/shop')
    else:
        return redirect('/login')

def view_cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        original_total = sum(parse_price(item.product.price) * item.quantity for item in cart_items)
        
        # Apply 70% Discount (Pink Summer Sale)
        discount_amount = original_total * 0.7
        final_total = original_total - discount_amount
        
        context = {
            'cart_items': cart_items,
            'original_total': original_total,
            'discount_amount': discount_amount,
            'total_price': round(final_total, 2)
        }
        return render(request, 'cart.html', context)
    else:
        return redirect('/login')

@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        messages.success(request, "Cart updated successfully.")
    return redirect('/cart')

@login_required
def delete_cart_item(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
        cart_item.delete()
        messages.success(request, "Item removed from cart.")
    return redirect('/cart')

def account(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = MyChngFrm(request.POST, instance=request.user)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, 'Profile updated successfully')
                except Exception:
                    messages.error(request, 'Profile could not be updated')
        else:
            form = MyChngFrm(instance=request.user)
        return render(request, 'account.html', {'form': form})
    else:
        return redirect('/login')

@csrf_exempt
def initiate_payment(request):
    if request.method == "POST":
        try:
            amount_str = request.POST.get("amount", "0")
            # Calculate amount in paise correctly, handling potential decimals
            amount = int(round(parse_price(amount_str) * 100))
            address = request.POST.get('address', '')
            client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET))

            payment_data = {
                "amount": amount,
                "currency": "INR",
                "receipt": "order_receipt",
                "notes": {
                    "email": request.user.email,
                },
            }

            order = client.order.create(data=payment_data)

            response_data = {
                "id": order["id"],
                "amount": order["amount"],
                "currency": order["currency"],
                "key": settings.RAZORPAY_API_KEY,
                "name": "GlamHub Cosmetics",
                "description": "Payment for Your Order",
                "image": "https://yourwebsite.com/logo.png",
            }
            
            cart_items = CartItem.objects.filter(user=request.user)
            for cart in cart_items:
                Order.objects.create(user=request.user, product=cart.product, quantity=cart.quantity, payment_status='success', address=address)

            CartItem.objects.filter(user=request.user).delete()

            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return redirect('/payment-success')

def payment_success(request):
    return render(request, "payment_success.html")

def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by("-date_ordered")
    return render(request, "my_orders.html", {"orders": orders})

def chngPwd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PwdChng(user=request.user, data=request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Password changed successfully')
            else:
                messages.error(request, 'Please correct the errors below')
        else:
            form = PwdChng(user=request.user)
        return render(request, 'chngPwd.html', {'form': form})
    return redirect('/login')

def product_detail(request, id):
    product = get_object_or_404(Item, id=id)
    related_products = Item.objects.filter(category=product.category).exclude(id=id)[:4]
    return render(request, 'product-details.html', {
        'product': product,
        'related_products': related_products
    })

def search(request):
    query = request.GET.get('q')
    allcate = Category.objects.all()
    if query:
        allitem = Item.objects.filter(name__icontains=query)
    else:
        allitem = Item.objects.all()
    return render(request, 'shop.html', {'allitem': allitem, 'allcate': allcate, 'query': query})

@login_required
def add_to_wishlist(request, id):
    product = get_object_or_404(Item, id=id)
    wishlist_item, created = WishlistItem.objects.get_or_create(product=product, user=request.user)
    if created:
        messages.success(request, f"{product.name} added to wishlist.")
    else:
        messages.info(request, f"{product.name} is already in your wishlist.")
    
    # Redirect back to the page the user was on
    next_url = request.GET.get('next', '/')
    return redirect(next_url)

@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_wishlist(request, id):
    wishlist_item = get_object_or_404(WishlistItem, id=id, user=request.user)
    wishlist_item.delete()
    messages.success(request, "Item removed from wishlist.")
    return redirect('/wishlist')
