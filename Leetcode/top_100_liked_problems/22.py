'''
22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

()()
(())
'''
class Solution(object):
    def generateParenthesis(self, n):
        ans = []
        s = ''
        l = 0
        r = 0
        def backtrack(s, l, r):
            if len(s) == 2 * n:
                ans.append(s)
                return
            if l < n:
                backtrack(s+'(', l+1, r)
            if r < l:
                backtrack(s+')', l, r+1)

        backtrack(s,l,r)
        return ans
print(Solution.generateParenthesis(Solution,3))