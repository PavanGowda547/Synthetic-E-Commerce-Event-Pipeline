"""
One-time seed generator.

Reads data/seed/categories.json (hand-authored taxonomy) and produces the
predefined datasets that the event generator consumes at runtime:

    data/predefined/products.json
    data/predefined/users.json

Why this is a separate, one-time step instead of generating products/users
on the fly inside the event generator:
  - The event generator should be deterministic given a catalog + seed. If
    it invented products every run, product_id/category relationships
    would not be stable across bronze partitions written on different days.
  - It mirrors a real pipeline: a "master data" catalog that changes rarely,
    versus a high-volume event stream that references it by foreign key.

Run:
    python data/seed/generate_catalog.py --num-products 4000 --num-users 20000
"""
import argparse
import json
import random
import uuid
from pathlib import Path

from faker import Faker

SEED_DIR = Path(__file__).parent
PREDEFINED_DIR = SEED_DIR.parent / "predefined"

BRANDS = [
    "Nimbus", "Trekker", "Zenlite", "Corevik", "Alta", "Northline", "Bravo",
    "Pixelor", "Homestead", "Vantra", "Ecomora", "Bluepeak", "Crestline",
    "Solace", "Urbanix", "Freshfield", "Ironclad", "Lumio", "Wavecrest",
    "Genuine", "Aarogya", "PureLeaf", "MetroMart", "DailyCo",
]

ADJECTIVES = [
    "Pro", "Max", "Lite", "Plus", "Ultra", "Classic", "Everyday", "Premium",
    "Compact", "Advanced", "Essential", "Deluxe",
]

def build_products(num_products: int, rng: random.Random) -> list[dict]:
    with open(SEED_DIR / "categories.json") as f:
        taxonomy = json.load(f)

    # Flatten (category, subcategory, leaf) triples so we can sample from them.
    leaves = []
    for category, subcats in taxonomy.items():
        for subcategory, leaf_types in subcats.items():
            for leaf in leaf_types:
                leaves.append((category, subcategory, leaf))

    products = []
    for i in range(num_products):
        category, subcategory, leaf = rng.choice(leaves)
        brand = rng.choice(BRANDS)
        adj = rng.choice(ADJECTIVES)
        name = f"{brand} {leaf} {adj}"

        # Base price band differs wildly by category -- this is what gives
        # the *catalog* a realistic price texture. The *popularity* skew
        # (a few products dominating sales) is applied later at sampling
        # time via a Pareto weight, not baked in here.
        price_band = {
            "Electronics": (500, 120000),
            "Clothing": (200, 6000),
            "Health & Medicine": (30, 2500),
            "Daily Necessities": (10, 800),
            "Home & Kitchen": (150, 45000),
            "Books & Stationery": (20, 1500),
            "Beauty": (99, 4000),
            "Sports & Fitness": (200, 25000),
            "Toys & Baby": (100, 5000),
            "Automotive": (100, 15000),
            "Pet Supplies": (50, 3000),
        }[category]
        price = round(rng.uniform(*price_band), 2)

        products.append({
            "product_id": f"P{i:06d}",
            "sku": str(uuid.uuid4())[:8].upper(),
            "name": name,
            "category": category,
            "subcategory": subcategory,
            "leaf_category": leaf,
            "brand": brand,
            "price": price,
            "currency": "INR",
            "in_stock_qty": rng.randint(0, 500),
        })
    return products

def main():
    parser = argparse.ArgumentParser(description="Seed the product & user catalogs")
    parser.add_argument("--num-products", type=int, default=4000)
    parser.add_argument("--num-users", type=int, default=20000)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    rng = random.Random(args.seed)
    PREDEFINED_DIR.mkdir(parents=True, exist_ok=True)

    products = build_products(args.num_products, rng)
    with open(PREDEFINED_DIR / "products.json", "w") as f:
        json.dump(products, f)
    print(f"Wrote {len(products)} products -> {PREDEFINED_DIR / 'products.json'}")

if __name__ == "__main__":
    main()
