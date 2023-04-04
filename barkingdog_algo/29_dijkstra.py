from heapq import heappop, heappush
import sys
input = sys.stdin.readline
INF = sys.maxsize


# velog
def boj1753():
    V, E = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(V+1)] # (w,v)
    d = [INF]*(V+1)  # 최단 거리
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w,v))

    queue = []
    d[start]=0
    heappush(queue, (0, start))
    while queue:
        w, v = heappop(queue)
        # 현재 정점에 대한 가중치가 다르면 넘어감
        if d[v]!=w: continue
        for nxt_w, nxt_v in graph[v]:
            # 현재 정점의 간선 중
            # 현재 정점을 거치는 것이 더 작으면 갱신
            if d[nxt_v] > d[v]+nxt_w:
                d[nxt_v] = d[v]+nxt_w
                heappush(queue, (d[nxt_v], nxt_v))

    for i in range(1, V + 1):
            print('INF' if d[i]==INF else d[i])


def boj11779():
    V = int(input())
    E = int(input())
    d = [INF]*(V+1)  # 최단 거리
    pre = [0]*(V+1) # 최단 거리 경로 복원
    graph = [[] for _ in range(V+1)] # (w,v)
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((w,v))
    s, e = map(int,input().split()) # 출발, 도착

    queue = []
    d[s]=0
    heappush(queue, (d[s], s))
    while queue:
        w, v = heappop(queue)
        # 현재 정점에 대한 가중치가 다르면 넘어감
        if d[v]!=w: continue
        for nxt_w, nxt_v in graph[v]:
            # 현재 정점의 간선 중
            # 현재 정점을 거치는 것이 더 작으면 갱신
            if d[nxt_v] > d[v]+nxt_w:
                d[nxt_v] = d[v]+nxt_w
                heappush(queue, (d[nxt_v], nxt_v))
                pre[nxt_v] = v # 이전 정점 저장

    print(d[e])
    path = []
    idx = e
    while idx!=s:
        path.append(idx)
        idx = pre[idx]
    path.append(idx)
    path.reverse()
    print(len(path))
    print(*path, sep=' ')


if __name__=='__main__':
    boj11779()