a = ['119', '97674223', '1195524421']
# should return false
b = ['123','456','789']
# should return true
c = ['12','123','1235','567','88']
# should return false
d = ['111113', '1112', '12']
# should return true

def solution(phone_numbers):
    phone_numbers.sort(key = lambda x: len(x))
    shortest_numbers = {}

    temp = phone_numbers.copy()
    # to keep track of numbers starting
    d = [True] * len(phone_numbers)

    for i in range(len(phone_numbers)):
        temp[i] = temp[i][:len(temp[0])]
        # make every phone numbers as short as 
        # the shortest number in the phone book
        if len(phone_numbers[i]) == len(phone_numbers[0]):
            if temp[i] not in shortest_numbers:
                shortest_numbers[temp[i]] = 1
            else:
                shortest_numbers[temp[i]] += 1
        else:
            # shortest number is not in front of any longer phone numbers
            if temp[i] not in shortest_numbers:
                d[i] = True
            else:
                d[i] = False
    for i in d:
        if i == False:
            return False
    return True

print(solution(a))
print(solution(b))
print(solution(c))
print(solution(d))