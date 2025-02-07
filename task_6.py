class Item:
    def __init__(self, calories, cost):
        self.calories = calories
        self.cost = cost
        self.ratio = calories / cost


def modify_items(items: dict):
    products = {}
    for name, value in items.items():
        cost = value["cost"]
        calories = value["calories"]
        products[name] = Item(calories, cost)
    return products


def greedy_algorithm(items: dict, money: int) -> dict:
    sorted_items = dict(sorted(items.items(), key=lambda item: item[1].ratio, reverse=True))
    current_money = money

    total_calories = 0
    total_products = {}

    for name, value in sorted_items.items():
        if current_money >= value.cost:
            current_money -= value.cost
            total_calories += value.calories
            total_products[name] = total_products.get(name, 0) + 1

        if current_money == 0:
            break

    return total_calories, total_products, money - current_money


def dynamic_programming(items: dict, money: int):
    items_values = list(items.values())
    items_names = list(items.keys())

    # Table to calculate max number of calories
    K = [[0 for x in range(money + 1)] for y in range(len(items) + 1)]

    # Table to save used products
    keep = [[0 for x in range(money + 1)] for y in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for x in range(1, money + 1):
            if items_values[i - 1].cost <= x:
                # If product is included
                if items_values[i - 1].calories + K[i - 1][x - items_values[i - 1].cost] > K[i - 1][x]:
                    K[i][x] = items_values[i - 1].calories + K[i - 1][x - items_values[i - 1].cost]
                    keep[i][x] = i - 1
                else:
                    K[i][x] = K[i - 1][x]
            else:
                K[i][x] = K[i - 1][x]

    total_items = {}
    current_money = money
    i = len(items)

    while i >= 0 and current_money > 0:
        if keep[i][current_money] != keep[i - 1][current_money]:
            product = items_names[keep[i][current_money]]
            total_items[product] = total_items.get(product, 0) + 1
            current_money -= items[product].cost
        i -= 1

    return K[len(items)][money], total_items, money - current_money


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

money = 100

print(greedy_algorithm(modify_items(items), money))
print(dynamic_programming(modify_items(items), money))