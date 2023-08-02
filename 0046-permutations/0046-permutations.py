class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            sub_lists = self.permute(nums)

            for s in sub_lists:
                s.append(n)
            result.extend(sub_lists)
            nums.append(n)
        return result
        
        