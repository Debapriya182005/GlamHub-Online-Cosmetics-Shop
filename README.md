<h1 align="center">
  💄 GlamHub — Online Cosmetics Shop
</h1>

<p align="center">
  A full-featured <strong>Django E-Commerce Web Application</strong> for cosmetics & beauty products.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Django-5.1-green?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQLite-Database-lightblue?style=for-the-badge&logo=sqlite&logoColor=white"/>
  <img src="https://img.shields.io/badge/Razorpay-Payment-blue?style=for-the-badge&logo=razorpay&logoColor=white"/>
</p>

---

## 🌟 About the Project

**GlamHub** is a fully functional e-commerce web application built with Django, designed for browsing and purchasing cosmetics and beauty products online. It features a complete shopping experience — from product browsing and wishlisting to cart management and online payment.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🛍️ **Product Catalogue** | Browse products by categories with labels like Bestseller, New, Top Rated, BOGO, Price Drop |
| 🔍 **Product Details** | Detailed product pages with images and descriptions |
| 🛒 **Shopping Cart** | Add/remove items, manage quantities |
| ❤️ **Wishlist** | Save favourite products for later |
| 👤 **User Authentication** | Register, Login, Change Password |
| 📦 **My Orders** | View order history and payment status |
| 💳 **Online Payment** | Integrated with **Razorpay** payment gateway |
| 🔐 **Secure Auth** | Custom user model with mobile number |
| 🎛️ **Admin Panel** | Full Django admin for managing products, orders & users |

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 5.1
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** SQLite3
- **Payment Gateway:** Razorpay
- **Authentication:** Django Custom User Model
- **Template Engine:** Django Templates

---

## 📁 Project Structure

```
GlamHub/
│
├── glamhub/              # Project configuration
│   ├── settings.py       # App settings (DB, static, Razorpay)
│   ├── urls.py           # Root URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── myapp/                # Main application
│   ├── models.py         # Customer, Item, Category, Cart, Order, Wishlist
│   ├── views.py          # All view logic
│   ├── urls.py           # App URL routes
│   ├── forms.py          # Django forms
│   ├── admin.py          # Admin panel config
│   └── migrations/       # Database migrations
│
├── templates/            # HTML Templates
│   ├── home.html         # Homepage
│   ├── shop.html         # Product listing
│   ├── product-details.html
│   ├── cart.html
│   ├── wishlist.html
│   ├── my_orders.html
│   ├── login.html
│   ├── custreg.html      # Customer registration
│   ├── account.html
│   ├── contact.html
│   ├── about-us.html
│   └── payment_success.html
│
├── static/               # CSS, JS, Images
├── media/                # Uploaded product/category images
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Debapriya182005/GlamHub-Online-Cosmetics-Shop.git
cd GlamHub-Online-Cosmetics-Shop

# 2. Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install django pillow django-mathfilters razorpay

# 4. Apply database migrations
python manage.py migrate

# 5. Create a superuser (for admin access)
python manage.py createsuperuser

# 6. Run the development server
python manage.py runserver
```

### 🌐 Open in browser
```
http://127.0.0.1:8000/
```

### 🔧 Admin Panel
```
http://127.0.0.1:8000/admin/
```

---

## 🗄️ Database Models

| Model | Description |
|---|---|
| `Customer` | Custom user model (extends AbstractUser) with mobile number |
| `Category` | Product categories with image |
| `Item` | Products with labels (Bestseller, New, BOGO, etc.) |
| `CartItem` | Items in a user's shopping cart |
| `Order` | Completed orders with payment info |
| `WishlistItem` | User's saved/favourite products |

---

## 💳 Payment Integration

GlamHub uses **Razorpay** for secure online payments.

To configure your own Razorpay keys, update in `glamhub/settings.py`:
```python
RAZORPAY_API_KEY = 'your_razorpay_key_here'
RAZORPAY_API_SECRET = 'your_razorpay_secret_here'
```

---

## 📸 Pages Overview

- 🏠 **Home** — Hero banner, featured products, categories
- 🛍️ **Shop** — Full product listing with filters
- 📄 **Product Detail** — Single product page
- 🛒 **Cart** — Shopping cart with quantity control
- ❤️ **Wishlist** — Saved products
- 📦 **My Orders** — Order history
- 👤 **Account** — Profile management
- 🔐 **Login / Register** — User authentication
- 📞 **Contact / About Us** — Info pages

---

## 👨‍💻 Developer

**Debapriya Mukherjee**
- GitHub: [@Debapriya182005](https://github.com/Debapriya182005)

---

<p align="center">Made with ❤️ using Django | GlamHub © 2025</p>
