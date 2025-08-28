
prices = {"laptop": 55000, "phone": 25000, "tablet": 18000}
max_price_product = max(prices, key=prices.get)
print(f"The product with the maximum price is: {max_price_product} at price {prices[max_price_product]}")
