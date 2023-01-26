class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter


        t_count = Counter(t)
        s_count = Counter()
        left = 0
        right = 0
        min_len = float('inf')
        min_str = ""
        while right < len(s):
            # Move right pointer to the right
            s_count[s[right]] += 1
            if all(s_count[c] >= t_count[c] for c in t_count):
                # All characters in t are included in the substring
                # Move left pointer to the right
                while left <= right:
                    if s_count[s[left]] > t_count.get(s[left], 0):
                        s_count[s[left]] -= 1
                        left += 1
                    else:
                        break
                # Update minimum substring length and substring
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_str = s[left:right+1]
            right += 1
        if min_str:
            return min_str
        else:
            return ""
