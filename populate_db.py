import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamhub.settings')
django.setup()

from myapp.models import Category, Item

def populate():
    # Categories
    categories = [
        {"name": "Skin Care", "about": "Premium products for your skin's health and glow."},
        {"name": "Makeup", "about": "Express your beauty with our professional makeup range."},
        {"name": "Hair Care", "about": "Nourish and style your hair with our organic formulas."}
    ]

    for cat_data in categories:
        cat, created = Category.objects.get_or_create(cat_name=cat_data["name"], defaults={"about": cat_data["about"]})
        if created:
            print(f"Created category: {cat.cat_name}")

    # Items
    skincare = Category.objects.get(cat_name="Skin Care")
    makeup = Category.objects.get(cat_name="Makeup")
    haircare = Category.objects.get(cat_name="Hair Care")

    items = [
        {"name": "Radiance Serum", "desc": "A powerful vitamin C serum for glowing skin.", "price": "1299", "cat": skincare},
        {"name": "Moisturizing Cream", "desc": "Deeply hydrates your skin for 24 hours.", "price": "850", "cat": skincare},
        {"name": "Velvet Lipstick", "desc": "Long-lasting matte finish in classic red.", "price": "599", "cat": makeup},
        {"name": "Silk Foundation", "desc": "Lightweight coverage for a natural look.", "price": "1100", "cat": makeup},
        {"name": "Argan Oil Shampoo", "desc": "Repairs damaged hair and adds shine.", "price": "750", "cat": haircare},
        {"name": "Nourishing Conditioner", "desc": "Leaves hair soft, smooth, and manageable.", "price": "699", "cat": haircare},
    ]

    for item_data in items:
        item, created = Item.objects.get_or_create(
            name=item_data["name"],
            defaults={
                "description": item_data["desc"],
                "price": item_data["price"],
                "category": item_data["cat"]
            }
        )
        if created:
            print(f"Created item: {item.name}")

if __name__ == "__main__":
    populate()
