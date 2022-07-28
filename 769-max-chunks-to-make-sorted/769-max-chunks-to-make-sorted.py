class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = arr[0]
        count = 0
        
        for i in range(len(arr)):
            if max_so_far<arr[i]:
                max_so_far = arr[i]

            if max_so_far == i:
                count+=1

        return count

        