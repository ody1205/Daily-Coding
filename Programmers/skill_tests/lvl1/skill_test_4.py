def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        budget -= i
        if budget < 0:
            break
        answer += 1
        
    return answer



d = [1,3,2,5,4]
b = 9
# should return 3
print(solution(d, b))

d1 = [2,2,3,3]
b1 = 10
print(solution(d1,b1))