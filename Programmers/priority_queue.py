'''
이중 우선순위 큐는 다음 연산을 할 수 있는 자료구조를 말합니다.

명령어	수신 탑(높이)
I 숫자	큐에 주어진 숫자를 삽입합니다.
D 1	큐에서 최댓값을 삭제합니다.
D -1	큐에서 최솟값을 삭제합니다.
'''

op1 = ['I 16','D 1']
op2 = ['I 7','I 5','I -5','D -1']

op3 = ['I 16', 'I -5643', 'D -1', 'D 1', 'D 1', 'I 123', 'D -1']
op4 = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

q = [-45, 45, 333]
def solution(operations):
    q = []
    for i in operations:
        a = i.split(' ')
        if a[0] == 'I':
            q.append(int(a[1]))
        if len(q) > 0:
            if a[0] == 'D' and a[1] == '1':
                q.pop(q.index(max(q)))
            if a[0] == 'D' and a[1] == '-1':
                q.pop(q.index(min(q)))
    if len(q) == 0:
        return [0,0]
    return [max(q), min(q)]

print(solution(op4))