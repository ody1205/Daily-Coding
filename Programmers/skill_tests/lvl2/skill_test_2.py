'''
프렌즈4블록
블라인드 공채를 통과한 신입 사원 라이언은 신규 게임 개발 업무를 맡게 되었다. 
이번에 출시할 게임 제목은 프렌즈4블록.
같은 모양의 카카오프렌즈 블록이 2×2 형태로 
4개가 붙어있을 경우 사라지면서 점수를 얻는 게임이다.


만약 판이 위와 같이 주어질 경우, 라이언이 2×2로 
배치된 7개 블록과 콘이 2×2로 배치된 4개 블록이 지워진다. 
같은 블록은 여러 2×2에 포함될 수 있으며, 지워지는 조건에 
만족하는 2×2 모양이 여러 개 있다면 한꺼번에 지워진다.



블록이 지워진 후에 위에 있는 블록이 아래로 떨어져 빈 공간을 채우게 된다.



만약 빈 공간을 채운 후에 다시 2×2 형태로 같은 모양의 블록이 
모이면 다시 지워지고 떨어지고를 반복하게 된다.


위 초기 배치를 문자로 표시하면 아래와 같다.
'''
def solution(m, n, board):
    ''' vertical =  m     horizontal -> =  n
    00 10
    C | C | B | D | E, 
    01 11
    A | A | A | D | E, 
    02 12
    A | A | A | B | F, 
    03 13
    C | C | B | B | F
    '''
    return find_remove(m,n,board)

def board_to_table(m,n,board):
    table = []
    for i in range(n):
        temp = ''
        for j in range(m):
            temp += board[j][i]
        table.append(temp)
    return table

def find_remove(m,n,board,count = 0):
    temp = []
    board = board_to_table(m,n, board)
    for i in range(n-1):
        for j in range(m-1):
            g = board[i][j]
            if g == 'X':
                pass
            elif g == board[i+1][j] and g == board[i+1][j+1] and g == board[i][j+1]:
                temp.append((i,j))
                temp.append((i,j+1))
                temp.append((i+1,j))
                temp.append((i+1,j+1))
    
    removed = list(set(temp))
    if removed:
        for i,j in removed:
            board[i] = board[i][:j] + 'X' + board[i][j+1:]
        for i in range(n):
            board[i] = board[i].replace('X','')
            board[i] = 'X' * (m - len(board[i])) + board[i]
        count += len(removed)
        return find_remove(n,m,board,count)
    else:
        return count

m = 4
n = 5	
b = ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']
print(solution(m,n,b))
# should print (14)
m1 = 6	
n1 = 6	
b1 = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
print(solution(m1,n1,b1))
# should print (15)