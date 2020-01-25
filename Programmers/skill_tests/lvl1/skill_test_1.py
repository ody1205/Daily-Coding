def solution(n, m):
    n1 = n
    m1 = m
    while(m1 != 0):
        temp = n1 % m1
        n1 = m1
        m1 = temp
    return [n1, int(n * m / n1)]


n = 3
m = 12
# should return [3, 12]

print(solution(n,m))

n1 = 2
m1 = 5
# should return [1, 10]
print(solution(n1,m1))