from itertools import permutations

def solution(numbers):
    answer = 0
    num = list(numbers)
    perm = []
    perm_list =[]
    for i in range(1,len(num)+1):
        perm.append(set(permutations(num,i)))
    for i in perm:
        for j in i:
            perm_list.append(''.join(j))
    perm_list = list(set(map(int,perm_list)))

    for i in perm_list:
        if i > 2:
            for j in range(2,i):
                if i%j == 0:
                    break
                elif i - 1 == j:
                    answer += 1
                    break
        elif i == 2:
            answer +=1

    return answer

a = '17'
b = '011'

print(solution(a))
print(solution(b))

