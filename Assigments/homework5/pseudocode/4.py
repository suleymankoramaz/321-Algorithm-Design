def MaxDiscount(sequence, discount_function):
    n = len(sequence)
    max_discount = [0] * n

    # Initialize the first element
    max_discount[0] = discount_function(sequence[0])

    # Dynamic Programming Loop
    for i in range(1, n):
        max_discount[i] = max(max_discount[i-1], 0) + discount_function(sequence[i])

    # Return the Maximum Discount
    return max(max_discount)