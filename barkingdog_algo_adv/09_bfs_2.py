# *
def boj2206():
    from collections import deque
    import sys
    input = sys.stdin.readline

    def BFS(a,b,c):
        queue = deque()
        queue.append((a,b,c)) # 시작
        while queue:
            x, y, z = queue.popleft()
            if x==N-1 and y==M-1: # 종료
                return visited[x][y][z]
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<N and 0<=ny<M:
                    # 벽이고 벽 부수기 가능
                    if board[nx][ny]==1 and z==0:
                        visited[nx][ny][1] = visited[x][y][0]+1
                        queue.append((nx,ny,1))

                    # 경로이고 방문하지 않았으면
                    elif board[nx][ny]==0 and visited[nx][ny][z]==0:
                        visited[nx][ny][z]=visited[x][y][z]+1
                        queue.append((nx,ny,z))

        return -1

    N, M = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(N)]
    # visited[x][y][0]: 벽 안 부순 경로, visited[x][y][1]: 벽 부순 경로
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][0]=1 # 시작
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    print(BFS(0,0,0))

# 포기
def boj9466():
    import sys
    input = sys.stdin.readline

    def iscycle(idx): # 사이클 확인
        cur = idx
        for _ in range(N):
            cur = graph[cur]
            if cur==idx:
                return True
        return False

    for _ in range(int(input())):
        N = int(input())
        graph = [[]]
        graph.extend(list(map(int, input().split())))
        answer = 0
        for i in range(1, N + 1):
            if not iscycle(i): answer+=1
        print(answer)

if __name__=='__main__':
    boj9466()