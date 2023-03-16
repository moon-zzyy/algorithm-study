import sys
input = sys.stdin.readline

# *
def boj1629():

    def pow(a, b):
        if b==1: # base condition
            return a%C

        val = pow(a, b//2)
        if b%2==0: return val*val % C
        else: return val*val*a % C

    A,B,C = map(int, input().split())
    print(pow(A,B))

# *
def boj11729():

    def hanoi(a, b, n):
        if n==1:
            print(a,b)
            return
        hanoi(a, 6-a-b, n-1)
        print(a, b)
        hanoi(6-a-b, b, n-1)

    K = int(input())
    print(2**K-1)
    hanoi(1, 3, K)

# *
# 참고: https://ggasoon2.tistory.com/11
def boj1074():
    N, r, c = map(int, input().split())
    answer=0
    while N>0:
        N-=1
        half = 2**(N)

        if r < half and c < half: # 1사분면
            answer+=0
        elif r < half and c >= half: # 2사분면
            answer += half*half
            c-=half
        elif r >= half and c < half: # 3사분면
            answer += 2*half*half
            r-=half
        else: # 4사분면
            answer += 3*half*half
            r-=half
            c-=half
    print(answer)


def boj17478():

    def func(x):
        if x==N:
            print(indent*x + '"재귀함수가 뭔가요?"')
            print(indent*x + '"재귀함수는 자기 자신을 호출하는 함수라네"')
            print(indent*x + '라고 답변하였지.')
            return

        print(indent*x + '"재귀함수가 뭔가요?"')
        print(indent*x + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print(indent * x + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        print(indent * x + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        func(x+1)

        print(indent * x + '라고 답변하였지.')

    N = int(input())
    indent = '____'
    print('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
    func(0)

# *
# 참고: https://fre2-dom.tistory.com/412
def boj1780():

    def func(x,y,n):
        check = board[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if board[i][j] != check: # 9개로 자르기
                    for a in range(3):
                        for b in range(3):
                            func(x+a * n//3, y+b * n//3, n//3)
                    return

        count[check]+=1 # 종이 세기

    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    count = {-1:0, 0:0, 1:0}
    func(0,0,N)
    print(*count.values(), sep='\n')


# velog
def boj2630():

    def func(x, y, n):
        check = board[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if board[i][j] != check:  # 4개로 자르기
                    for a in range(2):
                        for b in range(2):
                            func(x + a*n//2, y + b*n//2, n//2)
                    return
        count[check] += 1  # 종이 세기

    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    count = [0, 0] # 인덱스로 색 구분
    func(0, 0, N)
    print(*count, sep='\n')


def boj1992():
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(input().strip()))
    answer = ''

    def func(x, y, n):
        global answer
        check = board[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if board[i][j] != check:  # 4개로 자르기
                    answer+='('
                    for a in range(2):
                        for b in range(2):
                            func(x + a*n//2, y + b*n//2, n//2)
                    answer+=')'
                    return
        answer+=check


    func(0, 0, N)
    print(answer)


if __name__ == '__main__':
    boj1992()