FIRST_ITEM_PRICE = 1000
SUBSEQUENT_ITEM_PRICE = 120


def get_shipping_cost(quantity, first_item_price, subsequent_item_price):
    total_price = first_item_price + (quantity - 1) * subsequent_item_price
    return total_price


def main():
    item_amount = int(input())

    shipping_cost = get_shipping_cost(item_amount, FIRST_ITEM_PRICE, SUBSEQUENT_ITEM_PRICE)

    print(shipping_cost)


main()