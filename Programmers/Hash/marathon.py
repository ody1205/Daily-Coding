a = ['leo', 'kiki', 'eden']
b = ['eden', 'kiki']
# should return leo
c = ['mislav', 'stanko', 'mislav', 'ana']
d = ['stanko', 'ana', 'mislav']
# should return mislav

import collections

def solution(a, b):
    c = collections.Counter(a) - collections.Counter(b)
    return ''.join(list(c))

print(solution(a,b))
print(solution(c,d))