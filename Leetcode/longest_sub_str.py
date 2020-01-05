class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return  0
        
        dicts = {}
        max_length = start = 0

        for i in range(len(s)):
            if s[i] in dicts and start <= dicts[s[i]]:
                start = dicts[s[i]] + 1
            else:
                max_length = max(max_length, i - start + 1)
            dicts[s[i]] = i
        return (max_length)

s = Solution()
test = "abcabcbb"
print(s.lengthOfLongestSubstring(test))