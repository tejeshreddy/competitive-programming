class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = 0
        for n in nums:
            if n % 2 == 0:
                even_sum += n
        result = []
        for v, i in queries:
            current_val = nums[i]
            if current_val % 2 == 0:
                if (current_val + v) % 2 == 0:
                    even_sum += v
                else:
                    even_sum -= current_val
            else:
                if (current_val + v) % 2 == 0:
                    even_sum += (current_val + v)
            nums[i] += v
            result.append(even_sum)
        return result
                
            
            
        #     val = nums[i]
        #     if val + v % 2 == 0:
        #         even_sum += (v + val)
        #     else:
        #         even_sum -= val
        #     nums[i] = val + v
        #     result.append(even_sum)
        # return result
            
            
            
                
        
        