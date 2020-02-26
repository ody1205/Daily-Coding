'''
흰색 또는 검은색 모자를 쓴 사람들이 한 줄로 서있습니다. 
모든 사람은 바로 앞, 뒤에 있는 사람이 쓴 모자 색만 확인할 수 있으며, 
자신이 쓴 모자가 무슨 색인지는 알 수 없습니다. 물론, 가장 앞에 있는 사람은 바로 뒤에 있는 사람이 쓴 
모자색만 확인할 수 있으며, 가장 뒤에 있는 사람은 바로 앞에 있는 사람이 쓴 모자색만 확인할 수 있습니다. 
이때, 가장 앞에 있는 사람부터 자신이 본 검은색 모자 개수를 말하기 시작했습니다.

첫 번째 사람 : 나는 검은색 모자를 x개 볼 수 있어
두 번째 사람 : 나는 검은색 모자를 y개 볼 수 있어
...
마지막 사람 : 나는 검은색 모자를 z개 볼 수 있어
첫 번째 사람부터 순서대로 말한 검은색 모자 개수가 담긴 배열 black_caps가 매개변수로 주어집니다. 
확실하게 검은색 모자를 쓴 사람은 1, 확실하게 흰색 모자를 쓴 사람은 2, 어떤 모자를 썼는지 알 수 없는 
사람은 0으로 표시한 배열을 return 하도록 solution 함수를 완성해주세요.

제한사항
black_caps의 길이는 3 이상 200,000 이하입니다.
black_caps의 원소는 0 이상 2 이하인 정수입니다.
각 사람이 말한 검은색 모자 개수가 모순이 없는 경우만 입력으로 주어집니다.
입출력 예
black_caps	result
[1, 1, 2, 0]	[1, 1, 2, 1]
[1, 1, 1]	[0, 1, 0]
'''
def solution(b):
    answer = [0] * len(b)
    if b[0] == 1:
        answer[1] = 1
    else:
        answer[1] = 2
    
    for i in range(1,len(b)-1):
        if b[i] == 2:
            answer[i-1] = 1
            answer[i+1] = 1
            
    if b[-1] == 1:
        answer[-2] = 1
    else:
        answer[-2] = 2

    if b[2] == 2 and b[1] == 1:
        answer[0] = 1

    return answer

print(solution([1, 1, 2, 1]))