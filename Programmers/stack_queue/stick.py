def solution(arrangement):
    answer = 0
    stack = []

    for token in arrangement:
        if token == '(':
            stack.append(token)
            last = token
        else:
            if last == '(':
                stack.pop()
                answer += len(stack)
                last = token
            else:
                stack.pop()
                answer += 1

    return answer

a = '()(((()())(())()))(())'
print(solution(a))