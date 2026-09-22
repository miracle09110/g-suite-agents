"""Run this script to regenerate hotels_raw.csv."""
import csv, os, random

random.seed(42)

CITIES = [
    ("Manila",        "Philippines", "PHP", (2_500,  18_000)),
    ("Tokyo",         "Japan",       "JPY", (8_000,  65_000)),
    ("Paris",         "France",      "EUR", (80,        420)),
    ("London",        "UK",          "GBP", (75,        380)),
    ("Singapore",     "Singapore",   "SGD", (110,       650)),
    ("Sydney",        "Australia",   "AUD", (130,       520)),
    ("Bangkok",       "Thailand",    "THB", (600,     9_000)),
    ("Kuala Lumpur",  "Malaysia",    "MYR", (90,        900)),
    ("New York",      "USA",         "USD", (120,       700)),
    ("Barcelona",     "Spain",       "EUR", (70,        380)),
    ("Seoul",         "South Korea", "KRW", (80_000, 550_000)),
    ("Hong Kong",     "Hong Kong",   "HKD", (700,     5_500)),
]

PREFIXES  = ["Grand", "Royal", "The", "Luxury", "Premier", "Heritage",
             "Modern", "Urban", "Classic", "Plaza", "Elite", "Pacific"]
SUFFIXES  = ["Hotel", "Suites", "Inn", "Resort", "Lodge", "Boutique",
             "Manor", "Palace", "Tower", "Haven", "Residences", "Retreat"]
AMENITIES = [
    "Pool, WiFi, Gym",
    "WiFi, Restaurant, Bar",
    "Pool, Spa, WiFi",
    "Business Center, WiFi",
    "Pool, Gym, Restaurant",
    "Spa, WiFi, Bar",
    "Conference Room, WiFi",
    "Pool, WiFi, Breakfast Included",
    "Rooftop Bar, WiFi",
    "Airport Shuttle, WiFi, Pool",
]

rows = []
for city, country, currency, (lo, hi) in CITIES:
    for _ in range(random.randint(9, 11)):          # 9–11 hotels per city
        name   = f"{random.choice(PREFIXES)} {city} {random.choice(SUFFIXES)}"
        price  = random.randint(lo, hi) if random.random() > 0.10 else ""
        rows.append({
            "hotel_name":      name,
            "city":            city,
            "country":         country,
            "stars":           random.randint(2, 5)               if random.random() > 0.15 else "",
            "rating":          round(random.uniform(3.0, 5.0), 1) if random.random() > 0.15 else "",
            "price_per_night": price,
            "currency":        currency if price != "" else "",
            "amenities":       random.choice(AMENITIES)            if random.random() > 0.20 else "",
            "contact_email":   f"stay@{name.lower().replace(' ','')}.com"
                               if random.random() > 0.25 else "",
        })

# Add rows with completely missing critical fields (hotel_name or price blank)
for city, country, *_ in random.choices(CITIES, k=8):
    rows.append({
        "hotel_name": "", "city": city, "country": country,
        "stars": "", "rating": "", "price_per_night": "",
        "currency": "", "amenities": "", "contact_email": "",
    })

random.shuffle(rows)

out = os.path.join(os.path.dirname(__file__), "hotels_raw.csv")
fields = ["hotel_name","city","country","stars","rating",
          "price_per_night","currency","amenities","contact_email"]
with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    w.writerows(rows)

print(f"Generated {len(rows)} rows → {out}")
