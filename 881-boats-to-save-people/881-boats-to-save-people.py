class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people = sorted(people, reverse=True)
        
        boat = []
        result = 0
        l, r = 0, len(people) - 1
        
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                l += 1
            result += 1
        return result
                
            
            
        
        