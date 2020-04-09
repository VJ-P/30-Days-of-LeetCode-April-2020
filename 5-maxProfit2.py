# Best Time to Buy and Sell Stock II

# Say you have an array prices for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
# (i.e., buy one and sell one share of the stock multiple times).

# Note: You may not engage in multiple transactions at the same time
# (i.e., you must sell the stock before you buy again).

# Examples

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4. Then buy on 
# day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

# Input: [1,2,3,4,5]
# Output: 4

# Input: [7,6,4,3,1]
# Output: 0

def maxProfit2(prices):
    if len(prices) < 2:
        return 0
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            profit += prices[i + 1] - prices[i]
    return profit

print(maxProfit2([7,1,5,3,6,4]))
print(maxProfit2([1,2,3,4,5]))
print(maxProfit2([7,6,4,3,1]))