products = input().split("!")

while True:
    line = input()
    if line == "Go Shopping!":
        break
    command_arguments = line.split()
    command = command_arguments[0]
    product = command_arguments[1]

    if command == "Urgent":
        if product not in products:
            products.insert(0, product)
    elif command == "Unnecessary":
        if product in products:
            products.remove(product)
    elif command == "Correct":
        new_product = command_arguments[2]
        if product in products:
            index = products.index(product)
            products[index] = new_product
    elif command == "Rearrange":
        if product in products:
            products.remove(product)
            products.append(product)

print(", ".join(products))
