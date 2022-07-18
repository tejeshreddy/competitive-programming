class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def valid(s):
            stack = []
            for i in s:
                if i == "(":
                    stack.append(i)
                else:
                    if len(stack) > 0 and stack[-1] == "(":
                        stack.pop()
                    else:
                        stack.append(i)
            return len(stack) == 0
        
        
        def backtracking(s, o, c):
            if o > n or c > n:
                return
            if o == c and c == n and valid(s):
                result.append(s)
                return
            backtracking(s + "(", o + 1, c)
            backtracking(s + ")", o, c + 1)
        
        backtracking("", 0, 0)
        return result
            
            
        