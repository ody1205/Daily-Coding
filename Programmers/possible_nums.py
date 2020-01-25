def solution(given_num, target_num):
    d = [set() for i in range(8)]
    
    a = ''
    for i in range(len(d)):
        a += str(given_num)
        d[i].add(int(a))
    
    for i in range(1,8): # from 1 - 8
        for j in range(i): # when i = 1 j = 0, i = 2 j = 0 j = 1, ...
            for op1 in d[j]:
                for op2 in d[i-j-1]:
                    d[i].add(op1 + op2)
                    d[i].add(op1 - op2)
                    d[i].add(op1 * op2)
                    if op2 != 0:
                        d[i].add(op1//op2)
        if target_num in d[i]:
            return i + 1
    return -1

print(solution(5, 12))