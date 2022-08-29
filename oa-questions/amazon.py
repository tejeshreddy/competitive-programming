# https://leetcode.com/discuss/interview-question/872882/quora-coding-challenge-number-of-pairs-whose-sum-is-a-power-of-2
def power_three(a):
    ans = 0

    for i in range(0, 31):
        key = 3 ** i
        hmap = {}
        for j in range(len(a)):
            if key - a[j] in hmap:
                ans += hmap[key - a[j]]
            if key - a[j] == a[j]:
                ans += 1

            if a[j] in hmap:
                hmap[[a[j]]] = hmap[a[j] + 1]
            else:
                hmap[a[j]] = 1
    return ans

            
print(power_three([1, -1, 2, 3]))
print(power_three([2, 1, 8]))
