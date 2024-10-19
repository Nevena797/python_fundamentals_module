command = input()
total_price_without_taxes = 0
total_price_with_taxes = 0

while command != "special" and command != "regular":
    parts_prices_without_tax = float(command)
    if parts_prices_without_tax < 0:
        print(f"Invalid price!")
        command = input()
        continue
    elif parts_prices_without_tax > 0:
        total_price_without_taxes += parts_prices_without_tax
    command = input()

taxes = total_price_without_taxes * 0.20
if command == "special":
    if total_price_without_taxes > 0:
        total_price_with_taxes = total_price_without_taxes + taxes
        total_price_with_taxes = total_price_with_taxes - (total_price_with_taxes * 0.10)
    else:
        print("Invalid order!")
        exit(0)
if command == "regular":
    if total_price_without_taxes > 0:
        total_price_with_taxes = total_price_without_taxes + taxes
    else:
        print("Invalid order!")
        exit(0)

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_price_without_taxes:.2f}$")
print(f"Taxes: {taxes:.2f}$")
print("-----------")
print(f"Total price: {total_price_with_taxes:.2f}$")
