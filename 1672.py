class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest_wealth = 0
        for i in range(len(accounts)):
            counter = 0
            for j in range(len(accounts[i])):
                counter += accounts[i][j]
            if counter > richest_wealth:
                richest_wealth = counter
        return richest_wealth