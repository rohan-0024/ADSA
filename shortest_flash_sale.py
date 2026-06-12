import sys


def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)

    
    n = int(next(iterator))

    # 2. Parse the revenue array
    revenues = [int(next(iterator)) for _ in range(n)]

    # 3. Parse T (target revenue)
    target = int(next(iterator))

    # 4. Sliding Window / Two-Pointer Algorithm
    min_length = float("inf")
    current_sum = 0
    left = 0

    for right in range(n):
        # Add the current day's revenue to our window
        current_sum += revenues[right]

        # While the window meets or exceeds the target, try to shrink it from the left
        while current_sum >= target:
            window_length = right - left + 1
            if window_length < min_length:
                min_length = window_length

            # Shrink the window from the left side
            current_sum -= revenues[left]
            left += 1

    # 5. Format and print the result
    # If min_length was never updated, it means no window reached the target T
    result = min_length if min_length != float("inf") else 0
    print(f"Shortest Window: {result}")


if __name__ == "__main__":
    solve()
