def solution(n):
    a = list(str(n))
    a.sort(reverse=True)
    answer = int(''.join(a))    
    return answer

print(solution(118372))
# should return 873211