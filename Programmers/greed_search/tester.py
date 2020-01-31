def solution(answer):
    num1 = [1, 2, 3, 4, 5] # 5
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    answer_len = len(answer)
    
    counter = [0] * 3
    for i in range(answer_len):
        a = i%5
        b = i%8
        c = i%10
        
        if answer[i] == num1[a]:
            counter[0] += 1
        if answer[i] == num2[b]:
            counter[1] += 1
        if answer[i] == num3[c]:
            counter[2] += 1
    final = []
    
    for i in range(len(counter)):
        if max(counter) == counter[i]:
            final.append(i+1)
    
    return final

a = [1,2,3,4,5,1,2,3,4,5]
print(solution(a))
# should return 1

b = [1,3,2,4,2]
print(solution(b))
# should return 1,2,3