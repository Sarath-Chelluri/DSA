def maxprofit(cost):
    """
    accepts an array of int : prices of the stock
    buy the smallest value and sell when the profit is max
    input: [7,1,3,4,6,3]
    output: 5
    when no profit return 0
    """
    profit = []
    j = 0
    i = 0
    while j + 1 < len(cost):
        while i + 1 < len(cost) and cost[i + 1] < cost[i]:
            i += 1
        j = i
        while j + 1 < len(cost) and cost[j + 1] > cost[j]:
            j += 1
        profit.append(cost[j] - cost[i])
        i = j
    return max(profit)


print(maxprofit([7, 1, 5, 3, 6, 4]))
