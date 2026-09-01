import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agrigro.settings')
django.setup()

from store.models import Category, Product

CATEGORIES = [
    ("Seeds", "seeds"),
    ("Fresh Produce", "fresh-produce"),
    ("Farm Tools", "farm-tools"),
    ("Fertilizers", "fertilizers"),
]

# name, category_slug, description, price, stock, image_url
PRODUCTS = [
    ("Hybrid Tomato Seeds (50g)", "seeds", "High-yield hybrid tomato seed pack suited for both open field and polyhouse cultivation.", 149, 40, "PASTE_IMAGE_URL_HERE"),
    ("Organic Brinjal Seeds (25g)", "seeds", "Non-GMO brinjal seeds, disease-resistant variety, ideal for kitchen gardens.", 99, 60, "PASTE_IMAGE_URL_HERE"),
    ("Basmati Paddy Seeds (5kg)", "seeds", "Premium basmati paddy seeds with strong germination rate.", 899, 15, "PASTE_IMAGE_URL_HERE"),
    ("Fresh Alphonso Mangoes (1kg)", "fresh-produce", "Ripe Alphonso mangoes sourced directly from Ratnagiri orchards.", 450, 25, "PASTE_IMAGE_URL_HERE"),
    ("Farm-Fresh Tomatoes (1kg)", "fresh-produce", "Vine-ripened tomatoes, harvested within 24 hours of listing.", 40, 100, "PASTE_IMAGE_URL_HERE"),
    ("Organic Spinach Bunch (500g)", "fresh-produce", "Pesticide-free spinach grown using organic compost.", 35, 80, "PASTE_IMAGE_URL_HERE"),
    ("Red Onions (5kg)", "fresh-produce", "Storage-grade red onions, sun-dried and sorted.", 175, 60, "PASTE_IMAGE_URL_HERE"),
    ("Manual Seed Sower", "farm-tools", "Hand-held seed sower for uniform spacing in small plots.", 599, 20, "PASTE_IMAGE_URL_HERE"),
    ("Khurpi Hand Weeder", "farm-tools", "Sturdy steel khurpi for weeding and soil loosening.", 129, 50, "PASTE_IMAGE_URL_HERE"),
    ("Battery Sprayer (16L)", "farm-tools", "Rechargeable battery-operated sprayer for pesticide and fertilizer application.", 2499, 12, "PASTE_IMAGE_URL_HERE"),
    ("Vermicompost (10kg)", "fertilizers", "100% organic vermicompost enriched with earthworm castings.", 349, 35, "PASTE_IMAGE_URL_HERE"),
    ("NPK 19:19:19 Fertilizer (1kg)", "fertilizers", "Balanced water-soluble NPK fertilizer for all crop stages.", 189, 45, "PASTE_IMAGE_URL_HERE"),
]


def run():
    cat_map = {}
    for name, slug in CATEGORIES:
        cat, _ = Category.objects.get_or_create(slug=slug, defaults={"name": name})
        cat_map[slug] = cat
    print(f"Categories ready: {len(cat_map)}")

    created_count = 0
    updated_count = 0
    for name, cat_slug, desc, price, stock, image_url in PRODUCTS:
        obj, created = Product.objects.get_or_create(
            name=name,
            defaults={
                "category": cat_map[cat_slug],
                "description": desc,
                "price": price,
                "stock": stock,
                "image_url": image_url if image_url != "PASTE_IMAGE_URL_HERE" else "",
            },
        )
        if created:
            created_count += 1
        else:
            if image_url != "PASTE_IMAGE_URL_HERE" and image_url != obj.image_url:
                obj.image_url = image_url
                obj.save()
                updated_count += 1

    print(f"Products created: {created_count}")
    print(f"Products updated with new image_url: {updated_count}")
    print(f"Total products now: {Product.objects.count()}")


if __name__ == "__main__":
    run()
