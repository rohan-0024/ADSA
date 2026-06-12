import sys


def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    # 1. Parse the Catalog Size (m)
    m = int(next(iterator))

    # 2. Build the Catalog Hash Map: O(m) time and space
    # Mapping: product_id -> unit_price
    catalog = {}
    for _ in range(m):
        product_id = next(iterator)
        price = int(next(iterator))
        catalog[product_id] = price

    # 3. Parse the Cart Size (k)
    k = int(next(iterator))

    # 4. Calculate Total Cart Price: O(k) time
    total_cart_price = 0
    for _ in range(k):
        cart_id = next(iterator)
        quantity = int(next(iterator))

        # Retrieve the price from our hash map in O(1) average time
        price = catalog[cart_id]
        total_cart_price += price * quantity

    # 5. Print the formatted result
    print(f"Cart Total: {total_cart_price}")


if __name__ == "__main__":
    solve()
