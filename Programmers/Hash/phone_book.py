a = ['119', '97674223', '1195524421']
# should return false
b = ['123','456','789']
# should return true
c = ['111113', '1112', '12']
# should return true

def solution(a):
    a.sort(key = lambda x: len(x))
    for i in range(len(a)-1):
        y = a[i + 1][:len(a[0])]
        if a[0] == y:
            return False
    return True
    


print(solution(a))
print(solution(b))
print(solution(c))