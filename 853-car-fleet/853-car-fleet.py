class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_list = [(x, y) for x, y in zip(position, speed)]
        combined_list = sorted(combined_list, key=lambda x: x[0], reverse=True)
        
        stack = []
        for car in combined_list:
            if not stack:
                stack.append(car)
                continue
            last_car = stack[-1]
            if ((target - car[0])/car[1]) <= ((target - last_car[0])/last_car[1]):
                continue
            else:
                stack.append(car)
        return len(stack)
        
        