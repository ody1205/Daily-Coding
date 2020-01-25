a = ['leo', 'kiki', 'eden']
b = ['eden', 'kiki']
# should return leo

def solution(a,b):
    s = {}
    # count everyone in the marathon
    for i in a:
        if i not in s:
            s[i] = 1
        else:
            s[i] += 1
    # subtract everyone who finished the marathon from total count
    for i in b:
        if i in s:
            s[i] -= 1
    # return who didn't finish the marathon
    for i in s:
        if s[i] == 1:
            return i

print(solution(a,b))