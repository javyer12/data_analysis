products = [
   {"name": "apple", "price": 0.5, "stock": 50, "available": True},
   {"name": "banana", "price": 0.3, "stock": 100, "available": True},
   {"name": "orange", "price": 0.7, "stock": 30, "available": False},
   {"name": "grape", "price": 1.0, "stock": 20, "available": True}
]

print("Available products:")
for product in products:
    if product["available"]:
        print("-", product["name"])

product_chosen = input("\n  Choose a product:")
product_quantity = int(input("  Enter quantity:"))

# encontrar el producto en la lista, verificar que la cantidad no sea mayor al stock, y calcular el precio total
# for 
for product in products:
    if product["name"] == product_chosen:
        if product_quantity <= product["stock"]:
            total_price = product_quantity * product["price"]
            print(f"\n  Total price for {product_quantity} of {product_chosen}(s): ${total_price:.2f}")
        else:
            print(f"\n  Sorry, we only have {product['stock']} {product_chosen}(s) in stock.")
            response = input("Confirm if you want to proceed with the available stock (yes or no): ")
            if response.lower() == "yes":
                total_price = product['stock'] * product['price']
                print(f"\n  Total price for {product['stock']} of {product_chosen}(s): ${total_price:.2f}")
            else:
                print("\n  Order canceled.")
        break
    else:
        print("\n  Product not found.")

