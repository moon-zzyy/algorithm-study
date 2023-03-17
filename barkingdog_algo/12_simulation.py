import itertools
from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline


# 참고: https://velog.io/@ms269/%EB%B0%B1%EC%A4%80-15683-%EA%B0%90%EC%8B%9C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-Python
answer = 1e9
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
    for chicken in list(itertools.combinations(chickens, M)):
        temp = {h: 1e9 for h in houses} # 현재 M개의 치킨집과의 치킨거리
        for cx, cy in chicken:
            for hx, hy in houses: # 한 치킨집과 모든 집과의 거리
                temp[(hx, hy)] = min(temp[(hx, hy)], abs(cx - hx) + abs(cy - hy))
        dist.append(sum(temp.values())) # 현재 조합 치킨거리 합

    print(min(dist)) # 여러 치킨거리 중 최소


def boj11559():

    def BFS(i,j):
        queue = deque([i,j])
        match = deque([i,j])
        visited[i][j] = True
        while queue:
            x, y = queue.popleft()
            color = board[x][y]
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<N and 0<=ny<M:
                    if not visited[i][j] and board[nx][ny]==color:
                        visited[nx][ny]=True
                        queue.append((nx,ny))
                        match.append((nx,ny))

        flag=False # 연쇄 여부
        if len(match)>=4:
            flag=True
            delete()
        return flag

    def delete(match): # 4칸이상 블록 삭제
        for x, y in match:
            board[x][y] = '.'

    def down():
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
    while True:
        visited = [[False] * M for _ in range(N)]
        flag = False
        for i in range(N):
            for j in range(M):
                if board[i][j]!='.' and not visited:
                    flag = BFS(i, j)
        if not flag: break
        down()
        answer+=1

    print(answer)

if __name__ == '__main__':
    boj11559()
