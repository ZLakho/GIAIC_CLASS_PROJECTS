def run_shop():
    stock = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total = 0
    items = list(stock.items())

    for name, cost in items:
        qty = input(f"How many {name}s would you like?: ").strip()
        if qty.isdigit():
            total += int(qty) * cost

    print(f"Total bill: ${total}")

if __name__ == '__main__':
    run_shop()
