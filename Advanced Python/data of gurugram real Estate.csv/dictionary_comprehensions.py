items = ["apple", "banana", "cherry"]
prices = [0.5, 0.3, 0.2]

#Dictionary comprehension useing zip method
product_price = {item: price for item, price in zip(items, prices)}
print(product_price)

# Dictionary comprehension using enumerate method

product_price = {item: prices[i] for i, item in enumerate(items)}
print(product_price)

# Dictionary comprehension using range and length method

product_price = {items[i]: prices[i] for i in range(len(items))}
print(product_price)
