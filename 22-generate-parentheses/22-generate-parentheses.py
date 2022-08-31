class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        self.result = []
        def validate_parenthesis(s):
            stack = []
            for i in s:
                if i == "(":
                    stack.append(i)
                elif i == ")":
                    if len(stack) > 0 and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0

        def dfs(s):
            if len(s) > 2 * n:
                return
            elif len(s) == 2 * n and validate_parenthesis(s):
                self.result.append(s)
                return
            dfs(s + "(")
            dfs(s + ")")
        dfs("")
        return self.result
                
                
        
        
        
        
        
        
        
        