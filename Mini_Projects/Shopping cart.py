#First I will add a few products to the shopping cart using a dictionary
products = {
    "apple": 100,
    "lemon": 200,
    "potato": 400,
    "milk": 500,
}
#Now an empty cart 
cart = {}

#Now i will add functions for every choice and call them later
def show_products():
    print("\nAVAILABLE PRODUCTS: ")
    for items, price in products.items():
        print(f"{items} - ${price}")

def add_to_cart():
    show_products()
    item = input("\nEnter Product name to add: ").lower()
    if item in products:
        qty = int(input("Enter quantity: "))
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty
        print(f"{qty} x {item} added to cart.")
    else:
        print("Product not Found!")
def remove_from_cart():
    if not cart:
        print("YOur Cart is Empty!")
        return
    print("\nCart items: ")
    for item in cart:
        print(item)
    item = input("Enter product name to remove: ").lower()
    if item in cart:
        del cart[item]
        print(f"{item} removed from cart.")
    else:
        print("Product not found in cart!")

def view_cart():
    if not cart:
        print("\nYour cart is empty!")
        return
    print("\nCART ITEMS:")
    total = 0
    for item, qty in cart.items():
        price = products[item]
        total += price * qty
        print(f"{item} x {qty} = ${price * qty}")
    print(f"Total Price: ${total}")

#Now a while loop for the menu to run continuously until user exits.

while True:
    print("\n1. Show Products")
    print("\n2. Add to carts")
    print("\n3. Remove from cart")
    print("\n4.View Cart")
    print("\n5.Exit")

    choice = input("choose an option (1-5): ")

    if choice == "1":
        show_products()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        remove_from_cart()
    elif choice == "4":
        view_cart()
    elif choice == "5":
        print("Thanks for Shoppping")
        break
    else:
        print("Invalid choice. Please select a valid option.\n")