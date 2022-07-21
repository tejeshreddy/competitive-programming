class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        stack = []
        
        a_count = 0
        b_count = 0
        
        def check_stack():
            nonlocal a_count, b_count, stack
            if stack[-3] == stack[-2] == stack[-1]:
                turn_color = stack.pop()
                if turn_color == "A":
                    a_count += 1
                else:
                    b_count += 1
        
        for c in colors:
            if len(stack) < 3:
                stack.append(c)
            else:
                check_stack()
                stack.append(c)
        if len(stack) >= 3:
            check_stack()
        print(a_count, b_count)
        if a_count > b_count:
            return True
        return False
        