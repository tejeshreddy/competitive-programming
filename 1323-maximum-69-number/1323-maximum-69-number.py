class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        index = -1
        
        for i in range(len(num)):
            if num[i] == "6":
                index = i
                break
        
        if index != -1:
            num[index] = "9"
        return int("".join(num))
    
            
        
        