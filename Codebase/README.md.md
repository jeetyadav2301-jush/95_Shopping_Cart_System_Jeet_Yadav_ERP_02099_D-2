# 🛒 Shopping Cart System (PS 7)

A simple **console-based Shopping Cart System** developed in Python. The
program allows a user to view available products, add products to a
cart, remove products, check the cart, and generate a final bill with
discount and GST.

------------------------------------------------------------------------

## 📌 Project Overview

This project demonstrates basic Python programming concepts through a
small shopping cart application. Product details are stored in a
dictionary, while the cart keeps track of selected products and their
quantities.

## ✨ Features

-   **View Products** -- Display the available products and their
    prices.
-   **Add to Cart** -- Add a product with the required quantity.
-   **Remove from Cart** -- Remove a product completely from the cart.
-   **View Cart** -- Display cart items, quantities, item totals, and
    subtotal.
-   **Checkout** -- Generate an itemised final bill.
-   **Discount Calculation** -- Apply a 10% discount when the subtotal
    is more than ₹500.
-   **GST Calculation** -- Calculate 18% GST on the amount after
    discount.
-   **Input Validation** -- Handle invalid product names and non-integer
    quantities.

## 🧾 Product Catalogue

  Product      Price
  ---------- -------
  Pen            ₹10
  Notebook       ₹50
  Bag           ₹500

## 💰 Billing Rules

The program uses the following rules:

-   Discount rate: **10%**
-   Discount condition: discount is applied only when the subtotal is
    **greater than ₹500**.
-   GST rate: **18%**
-   GST is calculated on the subtotal after subtracting the discount.

**Calculation:**

``` text
Discount = 10% of Subtotal (only if Subtotal > ₹500)
GST = 18% of (Subtotal - Discount)
Grand Total = Subtotal - Discount + GST
```

## 🛠️ Requirements

-   Python 3
-   A terminal or command prompt (or any Python IDE)

No external Python libraries are required.

## ▶️ How to Run

1.  Download or copy the project file `shopping_cart.py`.

2.  Open a terminal or command prompt in the folder containing the file.

3.  Run:

    ``` bash
    python shopping_cart.py
    ```

    If your system uses the `python3` command, run:

    ``` bash
    python3 shopping_cart.py
    ```

4.  Follow the on-screen menu and enter a choice from **1 to 6**.

## 📋 Menu Options

    Choice Action
  -------- ------------------
         1 View products
         2 Add to cart
         3 Remove from cart
         4 View cart
         5 Checkout
         6 Exit

## 🧠 Python Concepts Used

-   Dictionaries for storing product prices and cart quantities
-   Functions to divide the program into reusable tasks
-   `while` loop for repeatedly displaying the menu
-   `if`, `elif`, and `else` for menu selection and validation
-   `for` loops to display products and cart items
-   `try` and `except` to handle invalid quantity input
-   String methods such as `strip()` and `title()`
-   `sum()` and dictionary methods such as `get()`
-   Main guard (`if __name__ == "__main__":`) to start the application

## 📂 Project Structure

``` text
Shopping-Cart-System/
└── shopping_cart.py
```

## ⚠️ Notes

-   Product names are matched without case sensitivity; for example,
    `pen` and `Pen` are accepted.
-   Quantity must be a whole number and at least 1.
-   Removing a product removes its entire quantity from the cart.
-   After a successful checkout, the cart is cleared.
-   The cart is stored in memory, so its contents are not saved after
    the program closes.

## 👩‍💻 Project

**Project Name:** Shopping Cart System\
**Project Code/Reference:** PS 7\
**Language:** Python\
**Application Type:** Console-based

------------------------------------------------------------------------

*Thank you for checking out the Shopping Cart System!*
