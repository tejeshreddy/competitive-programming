class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        stack = []
        
        a_count = 0
        b_count = 0
        
        def check_stack():
            nonlocal a_count, b_count, stack
            if len(stack) >= 3 and stack[-3] == stack[-2] == stack[-1]:
                turn_color = stack.pop()
                if turn_color == "A":
                    a_count += 1
                else:
                    b_count += 1
        
        for c in colors:
            check_stack()
            stack.append(c)
        check_stack()
        if a_count > b_count:
            return True
        return False
        