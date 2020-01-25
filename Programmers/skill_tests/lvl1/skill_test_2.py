def solution(s):
    answer = ''
    s = list(s)
    s.sort(reverse = True)
    
    return ''.join(s)

s = 'Zbcdefg'
# should return gfedcbZ

print(solution(s))