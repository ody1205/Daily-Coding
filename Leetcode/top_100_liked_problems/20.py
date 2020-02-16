'''
20. Valid Parentheses
Given a string containing just the characters 
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        opened = []
        s = list(s)
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        while s:
            top = s.pop(0)
            if top == '(' or top == '[' or top == '{':
                opened.append(top)
            else:
                if len(opened) != 0:
                    if opened[-1] == '(' and top == ')':
                        opened.pop()
                    elif opened[-1] == '[' and top == ']':
                        opened.pop()
                    elif opened[-1] == '{' and top == '}':
                        opened.pop()
                    else:
                        return False
                else:
                    return False
        if len(opened) != 0:
            return False
        return True
    if __name__ == '__main__':
        print(isValid(isValid, ")("))


class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'

                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack