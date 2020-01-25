def solution(n):
    answer = 0
    a = []
    for i in range(2,n+1):
        if i == 2:
            answer += 1
            a.append(i)
        if i == 3:
            answer += 1
            a.append(i)
        if i % 2 != 0 and i % 3 != 0:
            answer += 1
            a.append(i)
    return a



print(solution(20))
# should return 4
print(solution(5))
# should return 3