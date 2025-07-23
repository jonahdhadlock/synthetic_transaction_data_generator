# Synthetic Transaction Data Generator

This Python script generates a large, synthetic dataset of e-commerce transactions. It's designed for situations where real-world transactional data is unavailable due to privacy, security, or access constraints. The primary goal is to produce a robust dataset that mimics the characteristics of actual online sales, which can then be used for data analysis, model testing, or database performance evaluation.

---

## Project Goals

1.  **Create a Stand-in for Real Data**: To provide a reliable way to generate complex, structured data when real-world datasets are not an option.
2.  **Imitate E-commerce Metrics**: The generator is tuned to produce data that reflects realistic business metrics like **Average Order Value (AOV)** and **Average Selling Price (ASP)** across a wide variety of product categories.
3.  **Produce a Robust Output File**: The core value of this project is the generated `transactions.txt` file. This file serves as a ready-to-use data source for further analysis.

---

## Features

-   **Customizable Configuration**: Adjust parameters like the number of transactions, customers, and product details within the `get_configuration()` function.
-   **Weighted Product Categories**: The script uses a weighting system to simulate realistic purchasing patterns, where common items (like "Books" or "Office Supplies") are purchased more frequently than niche ones (like "Furniture").
-   **Dynamic Pricing & Quantity**: Each product category has a defined price and quantity range, and the script randomizes the values for each item in a transaction to ensure variety.
-   **Unique & Formatted IDs**: Employs `UUID4` for globally unique transaction IDs and a custom format for clean, readable product and customer IDs.
-   **Scalable**: Built to generate a high volume of transactions (tested with 50,000+) to test the robustness of data pipelines and analysis models.

---

## How to Use

1.  **Prerequisites**: Ensure you have Python 3.13 installed. The script uses only standard libraries (`uuid`, `datetime`, `random`), so no external packages are needed.
2.  **Run the Script**: Save the code as `main.py` and execute it from your terminal:
    ```bash
    python main.py
    ```
3.  **Check the Output**: The script will print a summary of the generation process and the final aggregate metrics to the console. The complete dataset will be saved in a file named `transactions.txt` in the same directory.

---

## Output File: `transactions.txt`

The main artifact of this project is `transactions.txt`. This file contains the detailed record of every generated transaction. The data is structured in a human-readable format, ready to be parsed by other scripts or tools for analysis.

### Example Transaction

Each transaction in the output file follows this format:

```
Transaction Number: 1234
Transaction ID: a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d
Customer ID: 05678
Date: 2025-07-22 14:30:15
Total Amount: $125.50
Items Purchased (Unique Products): 2
Total Quantity of All Items in Cart: 3
  Product ID: OFC0042, Quantity: 2, Price: $22.75
  Product ID: BOK0088, Quantity: 1, Price: $80.00
----------------------------------------------------
```

---

## Further Analysis

The `transactions.txt` file is intended to be the starting point for a data analysis workflow. The next logical step, which is beyond the scope of this generator, would be to write a parser (in **Python** with libraries like **pandas** or in **R**) to read this text file into a structured format like a DataFrame. From there, you could perform:

-   Customer segmentation
-   Sales forecasting
-   Market basket analysis
-   Product performance reviews
-   Economic modeling