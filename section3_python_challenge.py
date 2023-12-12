def calculate_pettychange(cost):
    available_coins = {
        2.0: 2,
        1.0: 6,
        0.5: 10,
        0.2: 4,
        0.1: 6,
        0.05: 7,
        0.02: 4,
        0.01: 6
    }
#Writing a dictionary to store the empty result
    result = {coin: 0 for coin in available_coins}

    remaining_cost = round(cost, 2)

#Iterating through available coins and deducting from remaining_cost
    for coin in sorted(available_coins.keys(), reverse=True):
        while remaining_cost >= coin and available_coins[coin] > 0:
            remaining_cost -= coin
            remaining_cost = round(remaining_cost, 2)
            available_coins[coin] -= 1
            result[coin] += 1

#If remaining cost is greater than 0, customer can't afford the cost
    if remaining_cost > 0:
        return "Can't afford this with the available petty change"

    return result


# Test cases
print(calculate_pettychange(12.50))
print(calculate_pettychange(16.89))
print(calculate_pettychange(16.90))
