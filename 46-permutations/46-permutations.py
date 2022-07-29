class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        if len(nums) == 1:
            result.append(nums[:])
            
        
        for i in range(len(nums)):
            n = nums.pop(0)
            
            sub_lists = self.permute(nums)
            
            for each_list in sub_lists:
                each_list.append(n)
            result.extend(sub_lists)
            nums.append(n)
        return result
            
            