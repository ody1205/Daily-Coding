A = [1, 3, 6, 4, 1, 2]
# sholud return 5
A1 = [-1, 1, 2, 3]
# should return 4
A2 = [-1, -3]
# should return 1


def solution(a):
    seen = [False] * len(a)
    for i in a:
        if 0 < i <= len(a):
            seen[i-1] = True
    for i in range(len(seen)):
        if seen[i] == False:
            return i + 1
    return len(a) + 1
    
    
    

print(solution(A))

print(solution(A1))

print(solution(A2))