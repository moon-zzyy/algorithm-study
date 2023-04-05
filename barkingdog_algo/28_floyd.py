import sys
input = sys.stdin.readline
INF = sys.maxsize


# velog
# https://claude-u.tistory.com/334
def boj11404():
    N = int(input()) # vertex
    M = int(input()) # edge
    d = [[INF]*(N+1) for _ in range(N+1)] # 최단 거리
    for _ in range(M):
        a, b, c = map(int, input().split())
        d[a][b] = min(d[a][b], c) # 노선 하나가 아닐 수 있음

    for i in range(1,N+1):
        d[i][i] = 0 # 자기자신으로 가는 비용

    # floyd algorithm
    for i in range(1,N + 1): # 거치는 정점
        for a in range(1,N + 1):
            for b in range(1,N + 1):
                # 시작과 도착 도시 다르고, 현재 정점을 거치는 것이 더 짧으면
                # d[a][b] = min(d[a][b], d[a][i]+d[i][b]) 이 시간복잡도가 더 크다
                if a!=b and d[a][b] > d[a][i]+d[i][b]:
                    d[a][b] = d[a][i]+d[i][b]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
                print(0 if d[i][j]==INF else d[i][j], end=' ')
        print()


def boj11780():
    N = int(input())
    M = int(input())
    d = [[1e9]*(N+1) for _ in range(N+1)] # 최단 거리
    nxt = [[0]*(N+1) for _ in range(N+1)] # 최단 거리 경로 복원
    for _ in range(M):
        a, b, c = map(int, input().split())
        d[a][b] = min(d[a][b], c)
        nxt[a][b] = b

    # floyd algorithm
    for i in range(1,N + 1):
        for s in range(1,N + 1):
            for t in range(1,N + 1):
                if s==t:
                    d[s][t] = 0
                    continue
                if d[s][t] > d[s][i]+d[i][t]:
                    d[s][t] = d[s][i]+d[i][t]
                    nxt[s][t] = nxt[s][i]

    for i in range(1, N + 1): # 최단거리
        for j in range(1, N + 1):
                print(0 if d[i][j]==1e9 else d[i][j], end=' ')
        print()
    for i in range(1, N + 1): # 최단거리경로
        for j in range(1, N + 1):
            if d[i][j]==1e9 or d[i][j]==0:
                print(0)
                continue
            # 경로 복원
            path = []
            idx = i
            while idx!=j:
                path.append(idx)
                idx = nxt[idx][j]
            path.append(j)
            print(len(path), end=' ')
            print(*path, sep=' ')


if __name__=='__main__':
    boj11780()