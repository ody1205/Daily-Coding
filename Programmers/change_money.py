def solution(n, money):
    table = [[0]*(n+1)] * len(money)
    for i in range(money[0], n+1, money[0]):
        table[0][i] = 1
    table[0][0] = 1
    for i in range(1, len(money)):
        for j in range(n+1):
            if j >= money[i]:
                table[i][j] = table[i-1][j] + table[i][j-money[i]]
            else:
                table[i][j] = table[i-1][j]


    return table[-1][-1]

n = 5
m =[1,2,5]
#should return 4

print(solution(n,m))