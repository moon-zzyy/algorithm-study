from collections import deque
from itertools import combinations, permutations
from copy import deepcopy
import sys
input = sys.stdin.readline


# 참고: https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-15683-%EA%B0%90%EC%8B%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
# answer = 1e9
def boj15683():
    def dfs(graph, depth):
        global answer

        if depth==len(cctvs): # 모든 cctv 방문
            answer = min(answer, sum([row.count(0) for row in graph])) # 최소 사각지대
            return

        x, y = cctvs[depth] # cctv 위치
        for dirs in mode[graph[x][y]]: # cctv 번호에 해당하는 방향
            temp = deepcopy(graph) # 복사

            for i in dirs: # 각 방향마다
                nx, ny = x, y

                while True: # 벽이나 가장자리 도달하기 전까지
                    nx+=dx[i]
                    ny+=dy[i]
                    if nx<0 or nx>=N or ny<0 or ny>=M: break
                    if temp[nx][ny]==6: break
                    elif temp[nx][ny]==0: temp[nx][ny]=-1 # 감시영역

            dfs(temp, depth+1) # 다음 cctv

    N, M = map(int, input().split())  # 세로, 가로
    board = [list(map(int, input().split())) for _ in range(N)] # 사무실
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    mode = {
        1: [[0],[1],[2],[3]],
        2: [[0,2],[1,3]],
        3: [[0,1],[1,2],[2,3],[0,3]],
        4: [[0,1,2],[0,1,3],[1,2,3],[0,2,3]],
        5: [[0,1,2,3]]
    }
    cctvs = [] # cctv 위치
    for i in range(N):
        for j in range(M):
            if 0< board[i][j] <6: cctvs.append((i,j))

    dfs(board, 0)
    print(answer)


# 1도 모르겠음...
# 참고: https://baejinsoo.github.io/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%20%EB%AC%B8%EC%A0%9C%ED%92%80%EA%B8%B0/BOJ_18808/
def boj18808():
    def pastable(x, y):
        for i in range(R):
            for j in range(C):
                if board[x + i][y + j] == 1 and sticker[i][j] == 1:
                    return False  # 붙일수없음
        for i in range(R):
            for j in range(C):
                if sticker[i][j] == 1:
                    board[x + i][y + j] = 1
        return True  # 붙임

    def rotate(s):
        rotated = [[0] * R for _ in range(C)]
        for i in range(R):
            for j in range(C):
                rotated[j][R - i - 1] = s[i][j]
        return rotated

    N, M, K = map(int, input().split())  # 노트북 세로, 가로, 스티커 개수
    board = [[0] * M for _ in range(N)]  # 노트북

    for i in range(K):
        R, C = map(int, input().split())  # 스티커 세로, 가로
        sticker = [list(map(int, input().split())) for _ in range(R)]

        for i in range(4):  # 회전
            flag = False

            if flag: break
            for i in range(N - R + 1):
                if flag: break
                for j in range(M - C + 1):
                    if pastable(i, j):  # 붙이면
                        flag = True
                        break
            sticker = rotate(sticker)
            R, C = C, R  # 행 열 바꾸기

    print(sum(map(sum, board)))  # 스티커 칸 수

# velog
# 다른풀이: https://velog.io/@toma/python-%EC%B9%98%ED%82%A8-%EB%B0%B0%EB%8B%AC-%EB%B0%B1%EC%A4%80-15686%EB%B2%88
def boj15686():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    houses, chickens = [], []  # 집과 치킨집 위치
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:  # 집
                houses.append((i, j))
            elif board[i][j] == 2:  # 치킨집
                chickens.append((i, j))

    dist = [] # 치킨거리 합
    for chicken in list(combinations(chickens, M)):
        temp = {h: 1e9 for h in houses} # 현재 M개의 치킨집과의 치킨거리
        for cx, cy in chicken:
            for hx, hy in houses: # 한 치킨집과 모든 집과의 거리
                temp[(hx, hy)] = min(temp[(hx, hy)], abs(cx - hx) + abs(cy - hy))
        dist.append(sum(temp.values())) # 현재 조합 치킨거리 합

    print(min(dist)) # 여러 치킨거리 중 최소

# *
# 참고: https://resilient-923.tistory.com/322
def boj11559():

    def BFS(i,j):
        queue = deque([(i,j)])
        match = deque([(i,j)])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            color = board[x][y]
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<N and 0<=ny<M:
                    if not visited[nx][ny] and board[nx][ny]==color: # 방문안함 + 같은색
                        visited[nx][ny]=True
                        queue.append((nx,ny))
                        match.append((nx,ny))

        flag=False # 연쇄 여부
        if len(match)>=4:
            flag=True
            delete(match)
        return flag

    def delete(match): # 4칸이상 블록 삭제
        for x, y in match:
            board[x][y] = '.'

    def down(): # 블록 내리키
        for i in range(6):
            for j in range(10, -1, -1):
                for k in range(11, j, -1):
                    if board[j][i] != "." and board[k][i] == ".":
                        board[k][i] = board[j][i]
                        board[j][i] = "."
                        break

    N, M = 12, 6
    board = [list(input().strip()) for _ in range(N)]
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    answer = 0

    while True: # 연쇄 없을 때까지
        visited = [[False] * M for _ in range(N)]
        is_chain = False # 연쇄 여부
        for x in range(N):
            for y in range(M):
                if board[x][y]!='.' and not visited[x][y]:
                    if BFS(x, y): is_chain=True
        if not is_chain: break
        down()
        answer+=1

    print(answer)

# *
# 참고: https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-14891-%ED%86%B1%EB%8B%88%EB%B0%94%ED%80%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
def boj14891():
    def rotate_right(n, d):
        if n>4 or wheels[n-1][2] == wheels[n][6]:
            return
        rotate_right(n+1, -d)
        wheels[n].rotate(d)

    def rotate_left(n, d):
        if n<1 or wheels[n][2] == wheels[n+1][6]:
            return
        rotate_left(n-1, -d)
        wheels[n].rotate(d)

    wheels = {}
    for i in range(1,5):
        wheels[i] = deque((map(int,input().strip())))
    for _ in range(int(input())):
        n, dir = map(int, input().split())
        rotate_right(n+1, -dir) # 현재 톱니바퀴의 오른쪽 회전
        rotate_left(n-1, -dir) # 현재 톱니바퀴의 왼쪽 회전
        wheels[n].rotate(dir) # 1: 시계방향으로 한 칸 회전

    answer = 0
    for i,wheel in enumerate(wheels.values()):
        answer+=int(wheel[0])*(2**i)
    print(answer)


# velog
# 참고: https://velog.io/@highcho/Algorithm-bakejoon-13335
def boj13335():
    N, W, L = map(int, input().split())
    arr = list(map(int, input().split()))
    bridge = [0]*W # 다리위 트럭
    answer = 0
    while bridge: # 마지막 들어가 빠져나갈 때까지
        answer+=1
        bridge.pop(0) # 다리 첫번째 요소
        if arr: # 트럭이 있으면 트럭 또는 빈 공간 채우기
            if sum(bridge)+arr[0]<=L:
                bridge.append(arr.pop(0))
            else:
                bridge.append(0)
    print(answer)

# *
# https://github.com/encrypted-def/basic-algo-lecture/blob/master/0x0D/solutions/14503.cpp
def boj14503():
    N, M = map(int, input().split())
    x,y, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1,0,1,0] # N, W, S, E
    dy = [0,-1,0,1]
    dir= {0:0,1:3,2:2,3:1}
    answer = 0
    d=dir[d] # 초기 방향
    
    while True:
        if board[x][y]==0:
            board[x][y]=-1 # 방문처리
            answer+=1
        cleaned = False # 네 방향 중 청소된 곳 여부
        for _ in range(4): # 반시계방향
            d = (d+1)%4
            if board[x+dx[d]][y+dy[d]]==0:
                x, y = x+dx[d], y+dy[d]
                cleaned=True
                break

        if not cleaned: # 청소안함
            if board[x-dx[d]][y-dy[d]]==1: # 후진시 벽
                break # 종료
            else: # 후진
                x, y = x-dx[d], y-dy[d]

    print(answer)

# 참고: https://pacific-ocean.tistory.com/363
def boj14499():
    def move(dir): # dice[1]: 위, dice[6]: 바닥
        if dir==1: # 동
            dice[1],dice[3],dice[4],dice[6] = dice[4],dice[1],dice[6],dice[3]
        elif dir==2: # 서
            dice[1],dice[3],dice[4],dice[6] = dice[3],dice[6],dice[1],dice[4]
        elif dir==3: #북
            dice[1],dice[2],dice[5],dice[6] = dice[5],dice[1],dice[6],dice[2]
        else: # 남
            dice[1],dice[2],dice[5],dice[6] = dice[2],dice[6],dice[1],dice[5]

    N, M, x, y, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dirs = list(map(int,input().split()))
    dx = [0,0,-1,1] # E, W, N, S
    dy = [1,-1,0,0]
    dice = [0]*7 # 주사위 숫자
    for dir in dirs:
        nx, ny = x+dx[dir-1], y+dy[dir-1]
        if 0<=nx<N and 0<=ny<M:
            x, y = nx, ny
            move(dir)
            if board[x][y] == 0:  # 주사위 숫자 복사
                board[x][y] = dice[6]
            else:  # 바닥 숫자 복사
                dice[6] = board[x][y]
                board[x][y] = 0
            print(dice[1])

# 삼성 sw
def boj3190():
    N = int(input())
    K = int(input())
    board = [[0]*(N) for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        board[x - 1][y - 1] = 1 # 사과
    L = int(input())
    move = {} # move[초]=방향
    for _ in range(L):
        t, d = input().split()
        move[int(t)] = d

    snake = [(0, 0)] # 뱀이 위치한 좌표
    dx = [0, 1, 0, -1]  # n, e, s, w
    dy = [-1, 0, 1, 0]
    dir = 1 # 현재 방향
    time = 0 # 현재 시간
    while True:
        time+=1
        y, x = snake[0] # 뱀 머리
        x, y = x+dx[dir], y+dy[dir] # 뱀 머리 이동
        if x<0 or x>=N or y<0 or y>=N: # 벽에 부딪힘
            break
        if (y, x) in snake: # 몸에 부딪힘
            break
        # 이동 가능
        snake.insert(0, (y, x))  # 뱀 머리 늘리기
        if board[x][y]==1: # 사과먹기
            board[x][y]=0
        elif board[x][y]==0: # 뱀 꼬리 지우기
            snake.pop()

        if time in move.keys():
            d = move[time]
            if d=='L': # 왼쪽으로 회전
                dir=(dir-1)%4
            else: # 오른쪽으로 회전
                dir=(dir+1)%4

    print(time)

# 벽을 3개 세운다 3중for문?
# 바이러스를 퍼뜨린다. bfs
# 안전영역을 구한다. 여기서 최대값 갱신
# 참고: https://heytech.tistory.com/368
def boj14502():
    def BFS(b):
        queue = deque(virus) # 바이러스 위치 미리 저장
        while queue:
            x, y = queue.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    if b[nx][ny] == 0:
                        b[nx][ny] = 2  # 바이러스 퍼짐
                        queue.append((nx,ny))
        count = 0 # 안전영역 개수
        for row in b:
            count += row.count(0)
        return count

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    safe = [] # 초기상태에서 안전 영역 리스트
    virus = [] # 초기상태에서 바이러스 영역 리스트
    answer = 0
    for x in range(N):
        for y in range(M):
            if board[x][y]==0:
                safe.append((x, y))
            elif board[x][y]==2:
                virus.append((x,y))

    for a,b,c in combinations(safe, 3): # 임의로 벽 3개 세우기
        board2 = deepcopy(board)
        board2[a[0]][a[1]]=1
        board2[b[0]][b[1]]=1
        board2[c[0]][c[1]]=1
        answer = max(answer, BFS(board2))

    print(answer)

# *
# 연산자 리스트 중 N-1개를 뽑는다 -> 시간초과
# 연산자별로 계산을 한다
# 최대값과 최소값을 갱신
def boj14888():
    def DFS(i, result, add, sub, mul, div):
        global max_value,min_value
        if i==N:
            max_value=max(max_value, result)
            min_value=min(min_value, result)
            return
        if add>0:
            DFS(i+1, result+arr[i], add-1, sub, mul, div)
        if sub>0:
            DFS(i+1, result-arr[i], add, sub-1, mul, div)
        if mul > 0:
            DFS(i + 1, result*arr[i], add, sub, mul-1, div)
        if div > 0:
            DFS(i + 1, int(result/arr[i]), add, sub, mul, div-1)

    N = int(input())
    arr = list(map(int, input().split())) # 피연산자
    add, sub, mul, div = map(int, input().split())
    max_value = -1e9
    min_value = 1e9
    DFS(1, arr[0], add, sub, mul, div) # 초기값은 첫번째 숫자
    print(max_value,min_value,sep='\n')


# *
# visited: True=스타트팀, False=링크팀
# 개수가 N/2가 되면 능력치 계산 후 최솟값 구하기
# answer = 1e9
def boj14889():
    def DFS(depth, idx):
        global answer
        if depth == N//2: # 팀 분리 완료
            A, B = 0, 0 # 각 능력치
            for i in range(N):
                for j in range(N):
                    if visited[i] and visited[j]:
                        A+=board[i][j] # 스타트
                    elif not visited[i] and not visited[j]:
                        B+=board[i][j] # 링크
            answer = min(answer, abs(A-B))
            return

        for i in range(idx, N):
            if not visited[i]:
                visited[i]=True # 스타트 팀
                DFS(depth+1, i+1)
                visited[i]=False # 링크 팀

    N = int(input())
    board = [ list(map(int, input().split())) for _ in range(N)]
    visited = [False]*N
    DFS(0, 0)
    print(answer)


# ***
# 참고: https://tmdrl5779.tistory.com/146
def boj15685():
    N = int(input())
    board = [[0]*101 for _ in range(101)] # 100*100 격자
    dx = [0, -1, 0, 1] # 0:오 1:위 2:왼 3:아래
    dy = [1, 0, -1, 0]
    for _ in range(N):
        y, x, d, g = map(int, input().split()) # y, x, 방향, 세대
        board[x][y] = 1 # 드래곤커브 표시

        curve = [d] # 커브 리스트
        for i in range(g):
            for j in range(len(curve)-1,-1,-1):
                nxt = (curve[j]+1)%4 # 다음 방향은 현재방향+1
                curve.append(nxt)

        for i in curve:
            x, y = x+dx[i], y+dy[i] # 드래곤 커브 표시
            board[x][y]=1

    answer = 0
    for i in range(100):
        for j in range(100):
            if board[i][j]==1 and board[i+1][j]==1 and board[i][j+1]==1 and board[i+1][j+1]==1 :
                answer+=1
    print(answer)


if __name__ == '__main__':
    boj15685()
