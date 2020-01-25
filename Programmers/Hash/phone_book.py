a = ['119', '97674223', '1195524421']
# should return false
b = ['123','456','789']
# should return true
c = ['12','123','1235','567','88']
# should return false
d = ['111113', '1112', '12']
# should return true

def solution(a):
    a.sort(key = lambda x: len(x))
    s = {}
    temp = a.copy()
    d = [True] * len(a)
    for i in range(len(a)):
        temp[i] = temp[i][:len(temp[0])]
        if len(a[i]) == len(a[0]):
            if temp[i] not in s:
                s[temp[i]] = 1
            else:
                s[temp[i]] += 1
        else:
            if temp[i] not in s:
                d[i] = True
            else:
                d[i] = False
    for i in d:
        if i == False:
            return False
    return True

print(solution(a))
print(solution(b))
print(solution(c))
print(solution(d))