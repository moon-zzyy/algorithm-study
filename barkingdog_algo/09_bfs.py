from collections import deque
import sys
input = sys.stdin.readline

# 참고: https://lakelouise.tistory.com/72
def boj1926():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
    visited = [[False]*M for _ in range(N)]
    count = [] # 정답 리스트

    def BFS(i,j):
        queue = deque([(i,j)])
        # queue.append((i,j))
        visited[i][j] = True
        area=0
        while queue:
            area+=1
            now = queue.popleft()
            for k in range(4):
                x, y = now[0]+dx[k], now[1]+dy[k]
                if 0<=x<N and 0<=y<M:
                    if board[x][y] and not visited[x][y]:
                        visited[x][y]=True
                        queue.append((x,y))
        return area
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visited[i][j]:
                count.append(BFS(i,j))
    print(len(count))
    print(max(count) if count else 0)

# 참고: https://yuna0125.tistory.com/61
def boj2178():
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().strip())))

    dx = [1,0,-1,0]
    dy = [0,1,0,-1]

    def BFS(i,j):
        queue = deque([(i,j)])
        # queue.append((i,j))
        while queue:
            now = queue.popleft()

            for k in range(4):
                x, y = now[0]+dx[k], now[1]+dy[k]
                if 0<=x<N and 0<=y<M:
                    if board[x][y]==1: # 벽이 아니고 아직 방문하지 않았다면
                        board[x][y]=board[now[0]][now[1]]+1 # (0,0)으로부터 거리
                        queue.append((x,y))

    BFS(0,0)
    print(board[-1][-1]) # (N-1,M-1)까지 최소거리


# *
def boj7576():
    N, M = map(int, input().split())
    board = []
    for _ in range(M):
        board.append(list(map(int, input().split())))

    if all(0 not in r for r in board): # 모두 익은 상태
        print(0)
        return

    queue = deque()
    def BFS():
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        while queue:
            now = queue.popleft()
            for k in range(4):
                x, y = now[0]+dx[k], now[1]+dy[k]
                if 0<=x<N and 0<=y<M:
                    if board[x][y]==0:
                        board[x][y]=board[now[0]][now[1]]+1 # 익은 일수+1 저장
                        queue.append((x,y))

    for i in range(M):
        for j in range(N):
            if board[i][j]==1:
                queue.append((i,j))
    BFS()
    print(*board,sep='\n')
    if any(0 in r for r in board): print(-1)# 모두 익지 못함 예외 처리
    else:
        print(max(map(max,board)))

# *
# 참고: https://chancoding.tistory.com/193
def boj1697():
    N, K = map(int, input().split())
    MAX = 100000 # N,K의 최대위치
    arr = [0]*(MAX+1) # 걸리는 시간

    def BFS(i):
        queue = deque([i])

        while queue:
            now = queue.popleft()
            if now==K: # 동생 위치
                print(arr[K])
                break
            for x in [now-1, now+1, now*2]: # 이동할 위치
                if 0<=x<=MAX:
                    if not arr[x]:
                        arr[x] = arr[now]+1 # 현재+1초 시간
                        queue.append(x)

    BFS(N)

# velog
def boj1012():
    def BFS(i, j):
        queue = deque([(i, j)]) # 처음 위치
        board[i][j] = 0 # 방문표시
        while queue:
            now = queue.popleft()
            for k in range(4):
                x, y = now[0] + dx[k], now[1] + dy[k]
                if 0 <= x < N and 0 <= y < M:
                    if board[x][y]==1: # 배추위치 확인
                        queue.append((x, y))
                        board[x][y] = 0 # 방문표시

    for _ in range(int(input())):
        M, N, K = map(int, input().split()) # 가로, 세로
        board = [[0] * M for _ in range(N)]
        for _ in range(K):
            j, i = map(int, input().split()) # 가로, 세로
            board[i][j] = 1

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        count = 0
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1: # 배추 있음
                    BFS(i, j)
                    count += 1 # 배추 군단++
        print(count)

# 참고: https://velog.io/@uoayop/BOJ-10026-%EC%A0%81%EB%A1%9D%EC%83%89%EC%95%BD-Python
def boj10026():
    def BFS(i, j, color):
        queue = deque([(i, j)]) # 처음 위치
        visited[i][j] = True # 방문표시
        while queue:
            now = queue.popleft()
            for k in range(4):
                x, y = now[0] + dx[k], now[1] + dy[k]
                if 0 <= x < N and 0 <= y < N:
                    if board[x][y]==color and not visited[x][y]:
                        visited[x][y] = True # 방문표시
                        queue.append((x, y))
                        # if color=='G': board[x][y]='R' # 왜 틀릴까

    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(input().strip()))
    visited = [[False]*N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    count = {'R':0,'G':0,'B':0, 'RG':0} # RG: R과 G 합친 것
    # 정상
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i, j, board[i][j])
                count[board[i][j]] += 1

    # 적록색맹
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j]=='G': board[i][j]='R'

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'R' and not visited[i][j]:
                BFS(i, j, 'R')
                count['RG'] += 1

    print(count['R']+count['G']+count['B'], count['RG']+count['B'])

# *
# velog
def boj7569():
    def BFS():  # 큐에는 익은 토마토가 들어있음
        while queue:
            z,x,y = queue.popleft()
            for dz,dx,dy in move:
                nx, ny, nz = x+dx, y+dy, z+dz
                if 0 <= nx < N and 0 <= ny < M and 0<= nz <H:
                    if board[nz][nx][ny] == 0:
                        board[nz][nx][ny] = board[z][x][y] + 1  # 익은 날짜+1 저장
                        queue.append((nz, nx, ny))

    M, N, H = map(int, input().split()) # 가로, 세로, 높이
    board = []
    for k in range(H):
        board.append([])
        for _ in range(N):
            board[k].append(list(map(int, input().split())))

    move = [(0, 0, 1), (0, 0, -1), (1, 0, 0), (0, 1, 0), (-1, 0, 0), (0, -1, 0)]
    queue = deque()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if board[k][i][j] == 1:
                    queue.append((k, i, j)) # 익은 토마토 큐에 삽입

    BFS()
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if board[k][i][j] == 0: # 덜 익은 토마토 존재
                    print(-1)
                    exit(0)
    print(max(max(map(max, r)) for r in board) - 1) # 최소 날짜


def boj7562():
    def BFS(i, j):
        queue = deque([(i, j)])
        board[i][j] = 1 # 처음 위치
        while queue:
            x, y = queue.popleft()
            if x==end[0] and y==end[1]:
                return board[x][y]-1

            for dx, dy in move:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:
                    if board[nx][ny] == 0:
                        queue.append((nx, ny))
                        board[nx][ny] = board[x][y]+1

    move = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,2),(1,2),(-1,-2),(1,-2)]
    for _ in range(int(input())):
        N = int(input())
        start = list(map(int, input().split()))
        end = list(map(int, input().split()))

        board = [[0]*N for _ in range(N)]
        print(BFS(start[0], start[1]))

# velog
# 참고: https://ywtechit.tistory.com/76
def boj4179():
    def BFS():
        while queue_fire: # 불의 이동
            x, y = queue_fire.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < R and 0 <= ny < C:
                    if arr[nx][ny]!='#' and fire[nx][ny]==0: # 벽이 아니고 아직 방문하지 않음
                        queue_fire.append((nx, ny))
                        fire[nx][ny] = fire[x][y]+1

        while queue_hoon: # 지훈의 이동
            x, y = queue_hoon.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < R and 0 <= ny < C: # 미로 안
                    if arr[nx][ny]!='#' and hoon[nx][ny]==0: # 벽이 아니고 아직 방문하지 않음
                        if fire[nx][ny]==0 or hoon[x][y]+1 < fire[nx][ny]: # 불이 없거나 불이 오기 전에 이동가능
                            queue_hoon.append((nx, ny))
                            hoon[nx][ny] = hoon[x][y]+1
                else: # 탈출
                    return hoon[x][y] # 시작이 1이기에 +1 필요없음

        return 'IMPOSSIBLE' # 탈출하지 못하면

    R, C = map(int, input().split())
    arr = [ list(input().strip()) for _ in range(R)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    fire = [[0] * C for _ in range(R)] # 불의 이동시간
    hoon = [[0] * C for _ in range(R)] # 지훈의 이동시간
    queue_fire, queue_hoon = deque(), deque()

    for i in range(R):
        for j in range(C):
            if arr[i][j]=='F': # 불 시작
                queue_fire.append((i,j))
                fire[i][j]=1
            if arr[i][j]=='J': # 지훈 시작
                queue_hoon.append((i,j))
                hoon[i][j]=1

    print(BFS())

# 포기
def boj5427():
    def BFS():
        while queue_fire: # 불의 이동
            x, y = queue_fire.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < h and 0 <= ny < w:
                    if arr[nx][ny]!='#' and fire[nx][ny]==0: # 벽이 아니고 아직 방문하지 않음
                        queue_fire.append((nx, ny))
                        fire[nx][ny] = fire[x][y]+1

        while queue_hoon: # 지훈의 이동
            x, y = queue_hoon.popleft()
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if 0 <= nx < h and 0 <= ny < w: # 미로 안
                    if arr[nx][ny]!='#' and hoon[nx][ny]==0: # 벽이 아니고 아직 방문하지 않음
                        if fire[nx][ny]==0 or hoon[x][y] < fire[nx][ny]: # 불이 없거나 불이 오기 전에 이동가능
                            queue_hoon.append((nx, ny))
                            hoon[nx][ny] = hoon[x][y]+1
                else: # 탈출
                    return hoon[x][y] # 시작이 1이기에 +1 필요없음

        return 'IMPOSSIBLE' # 탈출하지 못하면

    for _ in range(int(input())):
        w, h = map(int, input().split())
        arr = [ list(input().strip()) for _ in range(h)]

        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        fire = [[0] * w for _ in range(h)] # 불의 이동시간
        hoon = [[0] * w for _ in range(h)] # 지훈의 이동시간
        queue_fire, queue_hoon = deque(), deque()

        for i in range(h):
            for j in range(w):
                if arr[i][j]=='*': # 불 시작
                    queue_fire.append((i,j))
                    fire[i][j]=1
                elif arr[i][j]=='@': # 지훈 시작
                    queue_hoon.append((i,j))
                    hoon[i][j]=1

        print(BFS())


if __name__ == '__main__':
    boj5427()