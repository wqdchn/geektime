# @program: PyDemo
# @description: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# @author: wqdong
# @create: 2019-10-05 12:50

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0 or not s: return 0
        map, res, start = {}, 0, 0
        for i, char in enumerate(s):
            if char in map:
                start = max(start, map[char] + 1)
            res = max(res, i - start + 1)
            map[char] = i
        return res

    def lengthOfLongestSubstring2(self, s):
        if len(s) == 0 or not s: return 0
        xset, res, left, right = set(), 0, 0, 0
        while right < len(s):
            if s[right] not in xset:
                xset.add(s[right])
                right += 1
                res = max(res, len(xset))
            else:
                xset.remove(s[left])
                left += 1
        return res


s = Solution()

str = "abcabcbb"
print(s.lengthOfLongestSubstring(str))
print(s.lengthOfLongestSubstring2(str))
