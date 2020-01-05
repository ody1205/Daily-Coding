# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # write your code in Python 3.6
    if X >= Y:
        return 0
    num = ((Y-X)/D)
    if int(num) != num:
        return int(num) + 1
    return int(num)

X = 10
Y = 85
D = 30
print(solution(X,Y,D))
