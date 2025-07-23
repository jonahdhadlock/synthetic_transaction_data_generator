# Synthetic Transaction Data Generator
import uuid
import datetime
import random

def get_configuration() -> dict:
    """
    Consolidates and returns all configuration parameters for the simulation.

    Returns:
        dict: A dictionary containing all configuration settings.
    """
    # --- Configuration ---
    config = {
        "num_transactions": 50000,
        "num_customers": 10000,
        "max_items_per_transaction": 4,
        "output_filename": "transactions.txt",
        "product_categories": {
            "Groceries": {"prefix": "GRC", "weight": 4, "price_range": (1, 40), "quantity_range": (1, 3)},
            "Office Supplies": {"prefix": "OFC", "weight": 11, "price_range": (2, 45), "quantity_range": (1, 3)},
            "Art & Craft Supplies": {"prefix": "ART", "weight": 8, "price_range": (3, 80), "quantity_range": (1, 3)},
            "Movies & TV Shows": {"prefix": "MOV", "weight": 12, "price_range": (4, 35), "quantity_range": (1, 2)},
            "Clothing": {"prefix": "CLH", "weight": 9, "price_range": (12, 65), "quantity_range": (1, 2)},
            "Beauty": {"prefix": "BET", "weight": 9, "price_range": (2, 40), "quantity_range": (1, 2)},
            "Baby & Toddler": {"prefix": "BBY", "weight": 7, "price_range": (3, 45), "quantity_range": (1, 2)},
            "Pet Supplies": {"prefix": "PET", "weight": 8, "price_range": (4, 60), "quantity_range": (1, 2)},
            "Health & Personal Care": {"prefix": "HPC", "weight": 6, "price_range": (5, 40), "quantity_range": (1, 2)},
            "Books": {"prefix": "BOK", "weight": 12, "price_range": (4, 35), "quantity_range": (1, 2)},
            "Toys & Games": {"prefix": "TYS", "weight": 10, "price_range": (3, 80), "quantity_range": (1, 2)},
            "Kitchen & Dining": {"prefix": "KTD", "weight": 8, "price_range": (3, 80), "quantity_range": (1, 2)},
            "Children 4-12": {"prefix": "CHD", "weight": 6, "price_range": (4, 55), "quantity_range": (1, 2)},
            "Electronics": {"prefix": "ELC", "weight": 4, "price_range": (30, 650), "quantity_range": (1, 1)},
            "Jewelry": {"prefix": "JWL", "weight": 3, "price_range": (20, 110), "quantity_range": (1, 1)},
            "Automotive": {"prefix": "ATO", "weight": 2, "price_range": (25, 200), "quantity_range": (1, 1)},
            "Music & Instruments": {"prefix": "MUS", "weight": 2, "price_range": (10, 210), "quantity_range": (1, 1)},
            "Furniture": {"prefix": "FNT", "weight": 1, "price_range": (40, 270), "quantity_range": (1, 1)},
            "Industrial & Scientific": {"prefix": "INS", "weight": 1, "price_range": (80, 450), "quantity_range": (1, 1)},
            "Home Goods": {"prefix": "HME", "weight": 7, "price_range": (6, 55), "quantity_range": (1, 2)},
            "Sports & Outdoors": {"prefix": "SPT", "weight": 6, "price_range": (10, 90), "quantity_range": (1, 2)},
            "Tools & Utility": {"prefix": "TLS", "weight": 4, "price_range": (7, 100), "quantity_range": (1, 2)},
            "Garden & Patio": {"prefix": "GRD", "weight": 3, "price_range": (20, 110), "quantity_range": (1, 2)},
            "Home Improvement": {"prefix": "HMI", "weight": 5, "price_range": (12, 120), "quantity_range": (1, 2)},
            "Outdoor Recreation": {"prefix": "OUT", "weight": 5, "price_range": (10, 135), "quantity_range": (1, 2)},
            "Teens 13-19": {"prefix": "TNS", "weight": 5, "price_range": (5, 105), "quantity_range": (1, 2)},
            "Software": {"prefix": "SFT", "weight": 6, "price_range": (15, 90), "quantity_range": (1, 1)},
            "Digital Goods": {"prefix": "DGT", "weight": 12, "price_range": (1, 65), "quantity_range": (1, 1)},
        }
    }
    return config

def generate_product_id(prefix, product_number):
    """Generates a product ID with a 3-letter prefix and 4-digit number."""
    return f"{prefix}{str(product_number).zfill(4)}"

def create_product_catalog(product_categories) -> dict:
    """
    Creates a detailed product catalog from the category definitions.

    Args:
        product_categories (dict): A dictionary defining product categories.

    Returns:
        dict: A comprehensive catalog with individual product IDs.
    """
    product_catalog = {}
    for category, details in product_categories.items():
        prefix = details["prefix"]
        price_range = details.get("price_range", (10, 80))
        quantity_range = details.get("quantity_range", (1, 3))

        for i in range(1, 101):  # 100 different products per category
            product_id = generate_product_id(prefix, i)
            product_catalog[product_id] = {
                "category": category,
                "price_range": price_range,
                "quantity_range": quantity_range,
            }
    return product_catalog

def generate_transactions(num_transactions, num_customers, product_categories, product_catalog,
                          max_items_per_transaction) -> list:
    """
    Generates a list of synthetic customer transactions.

    Args:
        num_transactions (int): The number of transactions to generate.
        num_customers (int): The pool of customer IDs to draw from.
        product_categories (dict): The dictionary defining product categories and weights.
        product_catalog (dict): The pre-generated catalog of all products.
        max_items_per_transaction (int): The maximum number of unique product lines in a transaction.

    Returns:
        list: A list of transaction dictionaries.
    """
    transactions = []
    customer_ids = [f"{str(i).zfill(5)}" for i in range(1, num_customers + 1)]

    category_names = list(product_categories.keys())
    category_weights = [product_categories[name]["weight"] for name in category_names]

    for i in range(1, num_transactions + 1):
        transaction_id = str(uuid.uuid4())
        customer_id = random.choice(customer_ids)

        transaction_datetime = datetime.datetime(
            2025, 7, random.randint(1, 31),
            random.randint(0, 23),
            random.randint(0, 59),
            random.randint(0, 59)
        )

        items_purchased = []
        num_unique_products_in_transaction = random.randint(1, max_items_per_transaction)

        for _ in range(num_unique_products_in_transaction):
            chosen_category_name = random.choices(category_names, weights=category_weights, k=1)[0]
            products_in_category = [pid for pid, details in product_catalog.items() if
                                    details["category"] == chosen_category_name]

            if not products_in_category:
                continue

            product_id = random.choice(products_in_category)
            min_qty, max_qty = product_catalog[product_id]["quantity_range"]
            min_price, max_price = product_catalog[product_id]["price_range"]

            quantity = random.randint(min_qty, max_qty)
            price = round(random.uniform(min_price, max_price), 2)

            items_purchased.append({
                "product_id": product_id,
                "quantity": quantity,
                "price": price
            })

        if not items_purchased:
            continue

        total_amount = sum(item['quantity'] * item['price'] for item in items_purchased)

        transactions.append({
            "transaction_number": i,
            "transaction_id": transaction_id,
            "customer_id": customer_id,
            "date": transaction_datetime.strftime("%Y-%m-%d %H:%M:%S"),
            "total_amount": round(total_amount, 2),
            "items_purchased": items_purchased
        })
    return transactions


def write_transactions_to_file(transactions, filename):
    """
    Writes the generated transaction data to a text file.

    Args:
        transactions (list): A list of transaction dictionaries.
        filename (str): The name of the output file.
    """
    with open(filename, 'w') as f:
        for transaction in transactions:
            # File writing logic remains the same...
            f.write(f"Transaction Number: {transaction['transaction_number']}\n")
            f.write(f"Transaction ID: {transaction['transaction_id']}\n")
            f.write(f"Customer ID: {transaction['customer_id']}\n")
            f.write(f"Date: {transaction['date']}\n")
            # You could add formatting here too if desired, e.g., f"${transaction['total_amount']:,.2f}"
            f.write(f"Total Amount: ${transaction['total_amount']:.2f}\n")
            f.write(f"Items Purchased (Unique Products): {len(transaction['items_purchased'])}\n")
            total_items_in_cart = sum(item['quantity'] for item in transaction['items_purchased'])
            f.write(f"Total Quantity of All Items in Cart: {total_items_in_cart}\n")
            for item in transaction['items_purchased']:
                f.write(
                    f"  Product ID: {item['product_id']}, Quantity: {item['quantity']}, Price: ${item['price']:.2f}\n")
            f.write("-" * 52 + "\n")

    print(f"4. Successfully wrote {len(transactions):,} transactions to '{filename}'")

def calculate_and_print_metrics(transactions):
    """
    Calculates and prints the aggregate metrics (AOV, ASP) to the console.

    Args:
        transactions (list): A list of transaction dictionaries.
    """
    total_revenue = sum(t['total_amount'] for t in transactions)
    total_units_sold = sum(item['quantity'] for t in transactions for item in t['items_purchased'])
    actual_num_transactions = len(transactions)

    average_aov = total_revenue / actual_num_transactions if actual_num_transactions > 0 else 0
    average_asp = total_revenue / total_units_sold if total_units_sold > 0 else 0

    print("\n--- Aggregate Metrics ---")
    # --- ALL OF THESE LINES ARE CHANGED ---
    print(f"Total Number of Transactions: {actual_num_transactions:,}")
    print(f"Total Number of Units Sold: {total_units_sold:,}")
    print(f"Total Revenue: ${total_revenue:,.2f}")
    print(f"Average Order Value (AOV): ${average_aov:,.2f}")
    print(f"Average Selling Price (ASP): ${average_asp:,.2f}")

def run_simulation():
    """Orchestrates the entire data generation and reporting process."""
    # --- Setup ---
    print("Loading configuration...")
    config = get_configuration()

    # --- Execution Flow ---
    print("1. Creating product catalog...")
    product_catalog = create_product_catalog(config["product_categories"])

    print("2. Generating transaction data...")
    synthetic_data = generate_transactions(
        num_transactions=config["num_transactions"],
        num_customers=config["num_customers"],
        product_categories=config["product_categories"],
        product_catalog=product_catalog,
        max_items_per_transaction=config["max_items_per_transaction"]
    )

    print("3. Writing transactions to file...")
    write_transactions_to_file(synthetic_data, config["output_filename"])
    print("5. Calculating final metrics...")
    calculate_and_print_metrics(synthetic_data)

def main():
    """Main entry point to run the transaction data simulation."""
    run_simulation()

if __name__ == "__main__":
    main()