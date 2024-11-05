def min_coins(coins, target):
    if target == 0:
        return 0

    min = float('inf')

    for coin in coins:
        if coin <= target:
            subproblem_coins = min_coins(coins, target - coin)
            if subproblem_coins + 1 < min:
                min = subproblem_coins + 1

    return min
