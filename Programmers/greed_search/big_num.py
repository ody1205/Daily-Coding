def solution(number, k):
    stack = []
    
    for i,j in enumerate(number):
        while len(stack) > 0 and stack[-1] < j and k > 0:
            stack.pop()
            k -= 1
        stack.append(j)
        
    stack = stack[:-k] if k > 0 else stack
    
    return ''.join(stack)