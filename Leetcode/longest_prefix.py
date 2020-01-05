class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 or strs[0] == '':
            return ''
        if len(strs) == 1:
            return strs[0]
        strs.sort(key = lambda s: len(s))
        common = list(strs[0])
        for i in range(1, len(strs)):
            for j in range(len(common)):
                if strs[i][j] != common[j]:
                    return strs[i][:j]
        return ''

   


a = ["flower","flow","flight"]
b = ["dog","racecar","car"]

s = Solution()
print(s.longestCommonPrefix(b)) 