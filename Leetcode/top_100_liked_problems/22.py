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
    def generateParenthesis(self, N):
        ans = []
        S = ''
        left = 0
        right = 0
        def backtrack(S, left, right):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack(S,left,right)
        return ans
print(Solution.generateParenthesis(Solution,3))