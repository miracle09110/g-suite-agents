"""
Agent skills for the hotel CSV cleaner.

Each function is a custom ADK tool — the agent calls these to manipulate the data files.
"""

import csv
import os

# ── File paths ────────────────────────────────────────────────────────────────

DATA_DIR          = os.path.join(os.path.dirname(__file__), "data")
RAW_CSV           = os.path.join(DATA_DIR, "hotels_raw.csv")
CLEANED_CSV       = os.path.join(DATA_DIR, "hotels_cleaned.csv")
STANDARDIZED_CSV  = os.path.join(DATA_DIR, "hotels_standardized.csv")
EXCHANGE_RATES_CSV = os.path.join(DATA_DIR, "exchange_rates.csv")

# ── Currency reference ────────────────────────────────────────────────────────

def _load_exchange_rates() -> dict[str, float]:
    """Reads exchange_rates.csv and returns {currency_code: rate_to_usd}."""
    rates = {}
    with open(EXCHANGE_RATES_CSV, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            rates[row["currency_code"].strip().upper()] = float(row["rate_to_usd"])
    return rates


# ── Skill 1: View exchange rate reference ─────────────────────────────────────

def get_exchange_rates() -> dict:
    """Returns the full currency conversion reference table from exchange_rates.csv.

    Use this to check available currencies and their rates before standardizing.
    """
    try:
        rows = []
        with open(EXCHANGE_RATES_CSV, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                rows.append({
                    "code":         row["currency_code"],
                    "name":         row["currency_name"],
                    "rate_to_usd":  float(row["rate_to_usd"]),
                    "usd_per_unit": float(row["usd_to_currency"]),
                })
        return {
            "status": "success",
            "base_currency": "USD",
            "total_currencies": len(rows),
            "rates": rows,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


# ── Skill 2: Blank row cleaner ────────────────────────────────────────────────

def clean_blank_rows(csv_path: str = RAW_CSV) -> dict:
    """Removes hotel rows that are missing any critical field.

    Critical fields: hotel_name, city, price_per_night.
    A row is removed if ANY of these fields is blank or null.
    Saves the result to hotels_cleaned.csv.

    Args:
        csv_path: path to the CSV to clean (defaults to hotels_raw.csv)
    """
    try:
        with open(csv_path, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            fieldnames = reader.fieldnames

        critical = ["hotel_name", "city", "price_per_night"]
        kept, removed_names = [], []

        for row in rows:
            if all(row.get(field, "").strip() for field in critical):
                kept.append(row)
            else:
                removed_names.append(row.get("hotel_name") or "(no name)")

        with open(CLEANED_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(kept)

        return {
            "status":         "success",
            "saved_to":       CLEANED_CSV,
            "original_rows":  len(rows),
            "rows_kept":      len(kept),
            "rows_removed":   len(removed_names),
            "removed_hotels": removed_names,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


# ── Skill 3: Currency standardizer ───────────────────────────────────────────

def standardize_currencies(
    csv_path: str = CLEANED_CSV,
    target_currency: str = "USD",
) -> dict:
    """Converts every hotel's price_per_night to a single target currency.

    Reads exchange rates from exchange_rates.csv.
    Adds a new column (e.g. price_usd) and saves to hotels_standardized.csv.

    Args:
        csv_path:        path to the CSV to process (defaults to hotels_cleaned.csv)
        target_currency: 3-letter currency code to convert to (e.g. USD, EUR, PHP)
    """
    try:
        target = target_currency.strip().upper()
        rates  = _load_exchange_rates()

        if target not in rates:
            return {
                "status":    "error",
                "message":   f"Unknown currency '{target}'.",
                "available": sorted(rates.keys()),
            }

        with open(csv_path, newline="", encoding="utf-8") as f:
            reader    = csv.DictReader(f)
            rows      = list(reader)
            fieldnames = list(reader.fieldnames or [])

        price_col = f"price_{target.lower()}"
        if price_col not in fieldnames:
            fieldnames.append(price_col)

        target_rate = rates[target]
        converted, skipped = [], []

        for row in rows:
            currency  = row.get("currency", "").strip().upper()
            price_str = row.get("price_per_night", "").strip()

            try:
                price_original   = float(price_str)
                rate_to_usd      = rates.get(currency, 1.0)
                price_usd        = price_original * rate_to_usd
                price_converted  = round(price_usd / target_rate, 2)
                row[price_col]   = price_converted
            except (ValueError, TypeError):
                row[price_col] = ""
                skipped.append(row.get("hotel_name", "(unknown)"))

            converted.append(row)

        with open(STANDARDIZED_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(converted)

        return {
            "status":          "success",
            "saved_to":        STANDARDIZED_CSV,
            "target_currency": target,
            "rows_converted":  len(converted) - len(skipped),
            "rows_skipped":    len(skipped),
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
