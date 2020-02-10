'''
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
'''
def solution(name):
    answer = 0
    a = ord('A')
    idx = 0
    right = 0
    left = 0
    temp = []
    for i in range(len(name)):
        if ord(name[i]) - a > 13:
            temp.append(26 - (ord(name[i]) - a))
        else:
            temp.append(ord(name[i]) - a)
    while True:
        answer += temp[idx]
        temp[idx] = 0
        if sum(temp) == 0:
            break
        left = 1
        right = 1
        while temp[idx - left] <= 0:
            left += 1
        while temp[idx + right] <= 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right

    return answer

n = 'JEROEN' 
print(solution(n))
# should return 56 = (9 + 1) + (4 + 1) + (9 + 1) + (12 + 1) + (4 + 1) + (13)
n1 = 'JAN'
print(solution(n1))
# should return 23 = (9 + 1) + (13)
n2 = 'JAZ'
print(solution(n2))
# # should return 11 = (9 + 1) + (1)
n3 = 'AAA'
print(solution(n3))
# should return 1