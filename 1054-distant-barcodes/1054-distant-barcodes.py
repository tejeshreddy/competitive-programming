class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        hmap = collections.Counter(barcodes)
        result = [0] * len(barcodes)
        index = 0
        
        for key, value in hmap.most_common():
            for _ in range(value):
                if index >= len(barcodes):
                    index = 1
                result[index] = key
                index += 2
        return result
        
        
            
            
        