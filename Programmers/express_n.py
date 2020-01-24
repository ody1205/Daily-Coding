def solution(N, number):
    s = [ set() for x in range(8) ] 
    for i,x in enumerate(s, start=1):
        x.add( int( str(N) * i ) )

    for i in range(1, 8):
        for j in range(i):
            print('i',i)
            print('j',j)
            print(s)
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    print('op2',s[i-j-1])
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
                    print(s[i])

        if  number in s[i]:
            answer = i + 1
            break

    else:
        answer = -1

    return answer

print(solution(3,12))