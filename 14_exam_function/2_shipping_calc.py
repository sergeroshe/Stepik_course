FIRST_ITEM_PRICE = 1000
SUBSEQUENT_ITEM_PRICE = 120


def get_shipping_cost(quantity):
    total_price = FIRST_ITEM_PRICE + (quantity - 1) * SUBSEQUENT_ITEM_PRICE
    return total_price


def main():
    item_amount = int(input())

    shipping_cost = get_shipping_cost(item_amount)

    print(shipping_cost)


main()