import sys
input = sys.stdin.readline

# velog
def boj11404():
    N = int(input())
    M = int(input())
    d = [[1e9]*(N+1) for _ in range(N+1)] # 최단 거리
    for _ in range(M):
        a, b, c = map(int, input().split())
        d[a][b] = min(d[a][b], c)

    # floyd algorithm
    for i in range(1,N + 1):
        for s in range(1,N + 1):
            for t in range(1,N + 1):
                if s==t:
                    d[s][t] = 0
                    continue
                if d[s][t] > d[s][i]+d[i][t]:
                    d[s][t] = d[s][i]+d[i][t]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
                print(0 if d[i][j]==1e9 else d[i][j], end=' ')
        print()


def boj11780():
    N = int(input())
    M = int(input())
    d = [[1e9]*(N+1) for _ in range(N+1)] # 최단 거리
    nxt = [[0]*(N+1) for i in range(N+1)] # 최단 거리 경로 복원
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