import random

def change_competitor_prices(products: dict) -> dict:
    new_prices = {}

    for name, info in products.items():
        old_price = info["competitor_price"]

        change = random.randint(-10, 10)

        new_price = round(old_price * (1 + change / 100))

        new_price = max(1, new_price)

        new_prices[name] = new_price

    return new_prices
