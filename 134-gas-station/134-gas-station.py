class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        excess_gas = 0
        cur_gas = 0
        
        
        for i in range(len(gas)):
            excess_gas += gas[i] - cost[i]
            cur_gas += gas[i] - cost[i]
            
            if cur_gas < 0:
                cur_gas = 0
                start = i + 1
        
        if excess_gas >= 0:
            return start
        return -1