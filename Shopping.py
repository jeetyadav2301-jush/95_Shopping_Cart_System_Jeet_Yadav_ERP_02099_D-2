# Shopping Cart System
# Developer: Aashu
# Language: Python 3

PRICES = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500,
}
GST_RATE = 0.18
DISCOUNT_RATE = 0.10
CART = {}


def money(value):
    value = float(value)
    return str(int(value)) if value.is_integer() else str(round(value, 2))


def view_products():
    print("Available products:")
    for product, price in PRICES.items():
        print(f"- {product}: Rs.{price}")


def add_item(product_name, quantity):
    product = product_name.strip().title()
    if product not in PRICES:
        print(f"Invalid product. Available: {', '.join(PRICES.keys())}")
        return False

    if quantity < 1:
        print("Quantity must be at least 1.")
        return False

    CART[product] = CART.get(product, 0) + quantity
    subtotal = calculate_subtotal()
    print(f"{product} x{quantity} added | Cart subtotal: {money(subtotal)}")
    return True


def remove_item(product_name):
    product = product_name.strip().title()
    if product not in CART:
        print(f"{product} is not in the cart.")
        return False

    del CART[product]
    cart_summary = ", ".join(f"{item} x{qty}" for item, qty in CART.items()) if CART else "empty"
    print(f"{product} removed. Cart: {cart_summary}")
    return True


def view_cart():
    if not CART:
        print("Your cart is empty.")
        return

    print("Cart items:")
    for product, qty in CART.items():
        print(f"- {product} x{qty} = Rs.{PRICES[product] * qty}")


def calculate_subtotal():
    subtotal = 0
    for product, qty in CART.items():
        subtotal += PRICES[product] * qty
    return subtotal


def generate_bill():
    subtotal = calculate_subtotal()
    if subtotal > 500:
        discount = subtotal * DISCOUNT_RATE
    else:
        discount = 0

    gst = (subtotal - discount) * GST_RATE
    grand_total = subtotal - discount + gst

    return subtotal, discount, gst, grand_total


def checkout():
    if not CART:
        print("Your cart is empty.")
        return

    subtotal, discount, gst, grand_total = generate_bill()
    cart_summary = ", ".join(f"{product} x{qty}" for product, qty in CART.items())
    print(f"Cart: {cart_summary}")
    print(f"Subtotal: {money(subtotal)} | Discount: {money(discount)} | GST: {money(gst)} | Grand Total: {money(grand_total)}")
    CART.clear()


def main():
    print("Welcome to Shopping Cart System")
    while True:
        print("\n1. View products")
        print("2. Add item")
        print("3. Remove item")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            view_products()
        elif choice == "2":
            product = input("Enter product name: ")
            qty = int(input("Enter quantity: "))
            add_item(product, qty)
        elif choice == "3":
            product = input("Enter product name to remove: ")
            remove_item(product)
        elif choice == "4":
            view_cart()
        elif choice == "5":
            checkout()
        elif choice == "6":
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
