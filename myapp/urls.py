from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hmpage'),
    path('shop', views.shop, name='shoppage'),
    path('shop/<int:id>', views.shopCate, name='shopcatpage'),
    path('about', views.about, name='abtpage'),
    path('contact', views.contact, name='cntctpage'),
    path('login', views.custLog, name='loginpage'),
    path('logout', views.custLogout, name='logoutpage'),
    path('newcust', views.custReg, name="regpage"),
    path('addtocart/<int:id>', views.add_to_cart, name='addtocart'),
    path('cart', views.view_cart, name='crtpage'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/delete/<int:item_id>/', views.delete_cart_item, name='delete_cart_item'),
    path('account', views.account, name='account'),
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('payment-success/', views.payment_success, name='payment_success'),
    path("my-orders/", views.my_orders, name="my_orders"),
    path('chngpass', views.chngPwd, name="chngpass"),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('search', views.search, name='search'),
    path('wishlist', views.view_wishlist, name='view_wishlist'),
    path('wishlist/add/<int:id>', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/remove/<int:id>', views.remove_from_wishlist, name='remove_from_wishlist'),
]
