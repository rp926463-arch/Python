'''
Given a value V, if we want to make a change for V cents, and we have an infinite supply of each of 
C = { C1, C2, .., Cm} valued coins, what is the minimum number of coins to make the change? 
If it’s not possible to make a change, print -1.

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents 

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents

The minimum number of coins for a value V can be computed using the below recursive formula. 

If V == 0, then 0 coins required.
If V > 0
   minCoins(coins[0..m-1], V) = min {1 + minCoins(V-coin[i])} 
                               where i varies from 0 to m-1 
                               and coin[i] <= V
'''




# A Dynamic Programming based Python3 program to
# find minimum of coins to make a given change V
import sys

# m is size of coins array (number of
# different coins)
def minCoins(coins, m, V):
    table = [0 for i in range(V + 1)]
    table[0] = 0
    for i in range(1, V + 1):
        table[i] = sys.maxsize
    for i in range(1, V + 1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != sys.maxsize and sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    if table[V] == sys.maxsize:
        return -1
    return table[V]

# Driver Code
if __name__ == "__main__":

	coins = [9, 6, 5, 1]
	m = len(coins)
	V = 11
	print("Minimum coins required is ",
				minCoins(coins, m, V))

# This code is contributed by ita_c
