
# import math

# def canReach(c, x1, y1, x2, y2):

#     visited = set()

#     def checkperfectsquare(num):
#         root = math.sqrt(num)
#         if int(root + 0.5) ** 2 == num:
#             return True
#         else:
#             return False

#     def dfs(x, y):
#         if x > x2 or y > y2 or (x, y) in visited or checkperfectsquare(x + y):
#             return False
#         if x == x2 and y == y2:
#             return True
#         visited.add((x, y))
#         return dfs(x, x + y) or dfs(x + y, y) or dfs(x + c, y + c)
    


#     return "Yes" if dfs(x1, y1) else "No"

# print(canReach(1, 1, 4, 7, 6))
# print(canReach(1, 4, 3, 6, 4))
    


# arrival = [0, 0, 1, 4]
# street = [0, 1, 1, 0]
# 2 0 1 4

arrival = [0, 1, 1, 3, 3]
street = [0, 1, 0, 0, 1]
# 0 2 1 4 3
hmap = {}

main = []
first = []

for i, (a, s) in enumerate(zip(arrival, street)):
    hmap[(a, s)] = -1
    if s == 0:
        main.append((a, i))
    else:
        first.append((a, i))

cur_main = None
cur_first = None
prev = None
result = [0] * len(arrival)
timer = 0

while main and first:
    if not cur_main:
        cur_main = main.pop(0)
    if not cur_first:
        cur_first = main.pop(0)

    if prev == None:
        if cur_main < cur_first:
            prev = "Main"
            result[cur_main[1]] = max(timer, cur_main[0])
            timer = max(timer, cur_main[0])
        else:
            prev = "First"
            result[cur_first[1]] = max(timer, cur_first[0])
            timer = max(timer, cur_first[0])
    elif prev = "Main":



    

# prev_config = (-1, None)
# prev_main, prev_first = None, None

# while main and first:
#     if not prev_main:
#         prev_main = main.pop(0)
#     if not prev_first:
#         prev_first = first.pop(0)
    
#     if prev_main[0] == prev_first[0] and prev_main:
#         hmap[prev_first] = prev_config[0] + 1
#         prev_first = None
#     elif prev_main[0] < prev_first[0]:




    

    



