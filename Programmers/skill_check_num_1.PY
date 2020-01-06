'''
n명의 사람이 일렬로 줄을 서고 있습니다. n명의 사람들에게는 각각 1번부터 n번까지 번호가 매겨져 있습니다. n명이 사람을 줄을 서는 방법은 여러가지 방법이 있습니다. 
예를 들어서 3명의 사람이 있다면 다음과 같이 6개의 방법이 있습니다.

[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
사람의 수 n과, 자연수 k가 주어질 때, 사람을 나열 하는 방법을 사전 순으로 나열 했을 때, k번째 방법을 return하는 solution 함수를 완성해주세요.

제한사항
n은 20이하의 자연수 입니다.
k는 n! 이하의 자연수 입니다.
'''

n = 3
k = 5
#return [3,1,2]

# import itertools

def all_perms(elements):
    all_per = []
    if len(elements) <=1:
        return elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                all_per.append(perm[:i] + elements[0:1] + perm[i:])
    return all_per

def solution(n, k):
    a = list(range(1,n+1))
    # pos_comb = itertools.permutations(a)
    # answer = list(list(pos_comb)[k-1])
    # print(list(all_perms(a)))
    return 

print(solution(n, k))