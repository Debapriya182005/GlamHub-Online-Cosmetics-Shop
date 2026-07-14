import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glamhub.settings')
django.setup()

from myapp.models import Category, Item

def populate():
    # New Categories
    new_categories = [
        {"name": "Fragrances", "about": "Captivating scents for every occasion."},
        {"name": "Body Care", "about": "Pamper your body with our luxurious lotions and scrubs."},
        {"name": "Eye Care", "about": "Specialized treatments for the delicate eye area."},
        {"name": "Sun Care", "about": "Protect your skin from harmful UV rays."}
    ]

    cat_objs = {}
    for cat_data in new_categories:
        cat, created = Category.objects.get_or_create(cat_name=cat_data["name"], defaults={"about": cat_data["about"]})
        cat_objs[cat_data["name"]] = cat
        if created:
            print(f"Created category: {cat.cat_name}")
        else:
            print(f"Category already exists: {cat.cat_name}")

    # New Items
    new_items = [
        # Fragrances
        {"name": "Midnight Jasmine Perfume", "desc": "A seductive blend of jasmine and vanilla for evening wear.", "price": "2499", "cat": "Fragrances"},
        {"name": "Ocean Breeze Cologne", "desc": "Fresh and crisp scent reminiscent of a Mediterranean morning.", "price": "1850", "cat": "Fragrances"},
        {"name": "Rose Garden Mist", "desc": "Light and airy floral mist perfect for daily use.", "price": "999", "cat": "Fragrances"},
        
        # Body Care
        {"name": "Shea Butter Body Lotion", "desc": "Ultra-rich formula that melts into skin for intense hydration.", "price": "750", "cat": "Body Care"},
        {"name": "Himalayan Salt Scrub", "desc": "Exfoliates and revitalizes skin with natural minerals.", "price": "650", "cat": "Body Care"},
        {"name": "Lavender Body Wash", "desc": "Calming lavender scent that relaxes the mind and cleanses the body.", "price": "499", "cat": "Body Care"},
        
        # Eye Care
        {"name": "Anti-Aging Eye Cream", "desc": "Reduces the appearance of fine lines and dark circles.", "price": "1450", "cat": "Eye Care"},
        {"name": "Cooling Eye Gel", "desc": "Instantly depuffs and refreshes tired eyes.", "price": "899", "cat": "Eye Care"},
        {"name": "Brightening Eye Serum", "desc": "Infused with caffeine to wake up your look.", "price": "1200", "cat": "Eye Care"},
        
        # Sun Care
        {"name": "SPF 50 Sunscreen", "desc": "Broad-spectrum protection that's water-resistant and non-greasy.", "price": "950", "cat": "Sun Care"},
        {"name": "Aloe Vera After-Sun Gel", "desc": "Soothes and cools sun-exposed skin instantly.", "price": "550", "cat": "Sun Care"},
        
        # Adding some more to existing categories
        {"name": "Charcoal Face Mask", "desc": "Deep cleans pores and removes impurities for a clear complexion.", "price": "450", "cat": "Skin Care"},
        {"name": "Eyeliner Pen", "desc": "Precision tip for the perfect cat-eye every time.", "price": "399", "cat": "Makeup"},
        {"name": "Volume Mascara", "desc": "Dramatic volume and length without clumping.", "price": "650", "cat": "Makeup"},
        {"name": "Biotin Hair Serum", "desc": "Promotes thicker, fuller-looking hair with regular use.", "price": "1599", "cat": "Hair Care"}
    ]

    # Get existing categories too
    for cat in Category.objects.all():
        cat_objs[cat.cat_name] = cat

    for item_data in new_items:
        if item_data["cat"] in cat_objs:
            item, created = Item.objects.get_or_create(
                name=item_data["name"],
                defaults={
                    "description": item_data["desc"],
                    "price": item_data["price"],
                    "category": cat_objs[item_data["cat"]]
                }
            )
            if created:
                print(f"Created item: {item.name}")
            else:
                print(f"Item already exists: {item.name}")
        else:
            print(f"Category {item_data['cat']} not found for item {item_data['name']}")

if __name__ == "__main__":
    populate()
