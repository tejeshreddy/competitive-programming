"""
Title: 0014 - Longest Common Prefix
Tags: String
Time: O(n * k), k is the length of the common prefix
Space: O(1)
Source: https://leetcode.com/problems/longest-common-prefix/
Difficulty: Easy
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = None
        strs = sorted(strs, key=len)
        
        for string in strs:
            if prefix == None:
                prefix = string
            else:
                for i in range(min(len(prefix), len(string))):
                    if prefix[i] == string[i]:
                        
                        continue
                    if prefix[i] != string[i]:
                        prefix = prefix[:i]
                        break
        return "" if prefix == None else prefix
    
class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i in xrange(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]


# Time:  O(n * k), k is the length of the common prefix
# Space: O(k)
class Solution3(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        
        for chars in zip(*strs):
            if all(c == chars[0] for c in chars):
                prefix += chars[0]
            else:
                return prefix
            
        return prefix
