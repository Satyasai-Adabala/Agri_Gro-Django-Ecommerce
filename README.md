# Agri Gro — Django Ecommerce Project

A simple farm-to-cart ecommerce site built in Django: login, registration,
home, about, product search/filter, and add-to-cart.

## Features
- User registration & login (Django auth)
- Home page with featured products + category chips
- About page
- Product listing with **search** (`?q=`) and **category filter**
- Product detail page with related products
- Cart: add / increase / decrease / remove items, live total
- Django admin panel for managing Categories & Products
- Sample data seeder (`populate.py`) — 4 categories, 12 products

## Setup

```bash
# 1. Install Django (and Pillow, for product images)
pip install django pillow

# 2. Run migrations (a db.sqlite3 with sample data is already included,
#    but if you want a fresh DB, delete db.sqlite3 first)
python manage.py migrate

# 3. Seed sample products (safe to re-run, skips duplicates)
python manage.py shell -c "exec(open('populate.py').read())"
# or simply:
python populate.py

# 4. Create your own admin user (optional — one already exists)
python manage.py createsuperuser

# 5. Run the dev server
python manage.py runserver
```

Visit **http://127.0.0.1:8000/**

## Project structure

```
agrigro/
├── agrigro/          # project settings, root urls
├── store/            # main app: models, views, urls, admin, forms
│   └── models.py     # Category, Product, Cart, CartItem
├── templates/store/  # all HTML templates
├── static/css/       # style.css (Agri Gro theme)
├── media/products/   # uploaded product images go here
├── populate.py       # sample data seeder
└── manage.py
```

## Notes
- To add product photos, upload an image via `/admin/` on a Product — the
  card and detail page will automatically show it instead of the
  placeholder background.
- `ALLOWED_HOSTS` currently includes `127.0.0.1`, `localhost`, and
  `testserver`. Add your domain before deploying.
- `DEBUG = True` by default — turn this off for production.
