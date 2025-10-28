foods = []
prices = []
total = 0
while True:
    food = input("Enter food item (or 'done' to finish): ")
    if food.lower() == 'done':
        break
    else:
        price = float(input(f"Enter price for {food}: "))
        foods.append(food)
        prices.append(price)
print("\n SHOPPING CART ITEMS: ")
for food in foods:
    print(food, end=" ")
for price in prices:
    total += price
print(f"\nTotal Price: {total}")