# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

a = [2, 3, 1, 5]
def solution(A):
    # write your code in Python 3.6
    l = len(A) + 1
    #l + l-1 + l-2 + ... + l-l
    total = 0
    for i in range(1, l+1):
        total += i

    return total - sum(A)

print(solution(a))

