import itertools

def solution(numbers):
    pos_nums = []
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        comb = itertools.permutations(numbers,i)
        for j in list(comb):
            if ''.join(j) not in pos_nums:
                if int(''.join(j)) > 1 and ''.join(j)[0] != '0':
                    pos_nums.append(''.join(j))
    not_prime = []

    for num in pos_nums:
        if int(num) > 1:
            for i in range(2, int(num)):
                if (int(num) % i) == 0:
                    not_prime.append(int(num))
                    break

    return len(pos_nums) - len(not_prime)

print(solution('011'))