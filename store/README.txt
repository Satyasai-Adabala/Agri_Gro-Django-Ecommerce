# 🌱 Agri Gro — Farm-to-Cart E-Commerce Platform

A full-stack agricultural e-commerce web application built with **Python and Django**, designed to simulate a farm-to-cart marketplace where users can browse agricultural products, search and filter products, manage a shopping cart, and create accounts.

## 🚀 Project Overview

**Agri Gro** is a Django-based e-commerce platform developed from scratch to demonstrate real-world web application development using Django's **Models, Views, Templates, Forms, Authentication, ORM, and Admin Panel**.

The platform allows users to:

* Create an account and log in
* Browse agricultural products
* Search products by name or description
* Filter products by category
* View detailed product information
* Add products to a shopping cart
* Increase or decrease product quantities
* Remove products from the cart
* View cart totals
* Manage products through the Django Admin Panel

---

## ✨ Features

### 👤 User Authentication

* User registration with username, email, and password
* Secure password handling using Django Authentication
* Login and logout functionality
* Automatic cart creation for new users
* Protected cart pages using `@login_required`

### 🛒 Shopping Cart

* Add products to cart
* Increase/decrease product quantity
* Remove products from cart
* Automatic subtotal calculation
* Automatic total price calculation
* One cart per authenticated user

### 🔎 Product Search & Filtering

* Search products by name
* Search products by description
* Case-insensitive search
* Filter products by category
* Related products displayed on product detail pages

### 🛍️ Product Management

Products can include:

* Product name
* Category
* Description
* Price
* Stock
* Product image
* Creation date

### 🔐 Admin Dashboard

Django Admin provides an interface for managing:

* Categories
* Products
* Prices
* Stock
* Product images

---

## 🏗️ Project Structure

```text
Agri_Gro-Django-Ecommerce/
│
├── agrigro/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── store/
│       ├── base.html
│       ├── home.html
│       ├── about.html
│       ├── product_list.html
│       ├── product_detail.html
│       ├── login.html
│       ├── register.html
│       ├── cart.html
│       └── _product_card.html
│
├── static/
│   └── css/
│       └── style.css
│
├── media/
│   └── product/
│
├── manage.py
├── populate.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technology Stack

| Layer           | Technology             |
| --------------- | ---------------------- |
| Backend         | Python, Django 6.1     |
| Database        | SQLite                 |
| Frontend        | HTML, Django Templates |
| Styling         | Custom CSS             |
| Authentication  | Django Authentication  |
| Image Handling  | Pillow                 |
| Database Access | Django ORM             |
| Administration  | Django Admin           |
| Version Control | Git & GitHub           |

---

## 🗄️ Database Models

The application uses four main models:

### Category

Stores product categories such as Seeds, Farm Tools, Fertilizers, and Fresh Produce.

### Product

Stores product information including:

* Name
* Category
* Description
* Price
* Stock
* Image
* Created date

### Cart

Maintains one shopping cart for each authenticated user.

### CartItem

Represents products inside a user's cart and stores the selected quantity.

### Relationships

```text
User
  │
  └── One-to-One ──> Cart
                       │
                       └── One-to-Many ──> CartItem
                                              │
                                              └── Product
                                                   │
                                                   └── Category
```

---

## 🔄 Application Flow

Agri Gro follows Django's **MVT (Model–View–Template)** architecture.

```text
User
 │
 ▼
Browser Request
 │
 ▼
URL Routing
 │
 ▼
View
 │
 ├── Model / Django ORM
 │        │
 │        ▼
 │     Database
 │
 ▼
Template
 │
 ▼
HTML Response
 │
 ▼
User
```

### Example: Add to Cart

1. User clicks **Add to Cart**
2. Django receives the request
3. URL routing identifies the cart view
4. Authentication is checked
5. Product is retrieved using Django ORM
6. User's cart is retrieved or created
7. Cart item is created or quantity is increased
8. Cart total is recalculated
9. User is redirected back to the previous page

---

## 🔍 Search & Category Filtering

The product listing supports:

```text
/products/?q=tomato
```

and category filtering:

```text
/products/?category=seeds
```

Search checks both the **product name** and **description** using Django ORM queries.

---

## 🎨 Frontend

The frontend uses Django Template Language with template inheritance.

A shared `base.html` provides:

* Navigation bar
* Search bar
* Cart indicator
* Messages
* Footer

Individual pages extend the base template.

No Bootstrap or other CSS framework is used. The interface is styled using custom CSS.

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Satyasai-Adabala/Agri_Gro-Django-Ecommerce.git
```

### 2. Navigate to the project

```bash
cd Agri_Gro-Django-Ecommerce
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Populate sample data

```bash
python populate.py
```

### 8. Create an admin account

```bash
python manage.py createsuperuser
```

### 9. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

Admin dashboard:

```text
http://127.0.0.1:8000/admin/
```

---

## 📌 Key Django Concepts Demonstrated

This project demonstrates practical implementation of:

* Django MVT architecture
* Django ORM
* Model relationships
* ForeignKey
* OneToOneField
* Authentication
* User registration
* Login / Logout
* Forms and validation
* Function-based views
* Class-based LoginView
* URL routing
* Template inheritance
* Template partials
* Static files
* Media files
* ImageField
* Django Admin
* Query filtering
* Search using `Q` objects
* `get_or_create()`
* `get_object_or_404()`
* `@login_required`
* Database migrations
* Git and GitHub

---

## 📸 Project Screenshots

Screenshots can be added here to demonstrate:

* Home page
* Product listing
* Product details
* Login / Registration
* Shopping cart
* Django Admin

---

## 🔮 Future Improvements

Possible future enhancements include:

* Online payment integration
* Order management
* Order history
* Product reviews and ratings
* Wishlist
* Stock availability validation
* Product pagination
* REST API using Django REST Framework
* PostgreSQL database
* Cloud image storage
* Production deployment
* Email notifications

---

## 🎯 Project Purpose

Agri Gro was developed as a **portfolio and learning project** to gain practical experience in Python, Django, database design, authentication, e-commerce workflows, and full-stack web development.

It demonstrates how a complete web application can be designed and implemented using Django's built-in capabilities without relying on a dedicated e-commerce framework.

---

## 👨‍💻 Author

**Adabala Satya Sai**

GitHub: [@Satyasai-Adabala](https://github.com/Satyasai-Adabala)

---

## ⭐ Acknowledgement

Built as a hands-on Django project to understand and implement real-world e-commerce application architecture.
