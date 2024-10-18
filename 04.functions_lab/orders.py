def total_price(current_product, current_quantity):
    if current_product == "coffee":
        price = 1.50
    elif current_product == "coke":
        price = 1.40
    elif current_product == "water":
        price = 1.00
    elif current_product == "snacks":
        price = 2.00
    return current_quantity * price


produckts = input()
quantity = int(input())
result = total_price(produckts, quantity)
print(f"{result:.2f}")
