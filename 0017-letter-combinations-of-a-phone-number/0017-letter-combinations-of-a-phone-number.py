class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        
        result = []
        temp = [hmap[int(i)] for i in str(digits)]
        print(temp)
        while temp:
            curr = temp.pop(0)
            temp_result = []
            
            if len(result) == 0:
                result.extend([i for i in curr])
            else:
                for i in curr:
                    for j in result:
                        temp_result.append(j + i)
            
                result = temp_result
            
        return result
                
        