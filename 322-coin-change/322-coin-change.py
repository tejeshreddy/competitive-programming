class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        if amount == 0:
            return 0
        
        arr = [amount + 1] * (amount + 1)
        arr[0] = 0
        
        coins.sort()
        
        for i in range(len(arr)):
            for c in coins:
                if c <= i:
                    arr[i] = min(1 + arr[i - c], arr[i])
                else:
                    break

        return arr[amount] if arr[amount] != amount + 1 else -1
        