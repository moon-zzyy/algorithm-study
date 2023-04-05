from collections import deque
import sys
input = sys.stdin.readline
# MST: https://velog.io/@yoopark/baekjoon-1197

def boj11724():
    def BFS(start):
        queue = deque([start])
        visited[start]=True
        while queue:
            cur = queue.popleft()
            for v in graph[cur]:
                if not visited[v]:
                    visited[v]=True
                    queue.append(v)

    def DFS(start): # 재귀
        visited[start]=True
        for v in graph[start]:
            if not visited[v]:
                DFS(v)

    def DFS2(start):  # 비재귀
        stack = [start]
        visited[start] = True
        while stack:
            cur = stack.pop()
            for v in graph[cur]:
                if not visited[v]:
                    visited[v] = True
                    stack.append(v)

    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1) ]
    visited = [False]*(N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    count = 0
    for i in range(1,N+1):
        if not visited[i]:
            DFS2(i)
            count+=1
    print(count)


def boj1260():
    def BFS(start):
        queue = deque([start])
        visited[start] = True
        answer.append(start)
        while queue:
            cur = queue.popleft()
            for v in graph[cur]:
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
                    answer.append(v)

    def DFS(start):  # 재귀
        visited[start] = True
        answer.append(start)
        for v in graph[start]:
            if not visited[v]:
                DFS(v)

    N, M, V = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for node in graph: # 정점번호가 작은 것부터 방문
        node.sort()

    visited = [False] * (N + 1)
    answer = []
    DFS(V)
    print(*answer, sep=' ')
    visited = [False] * (N + 1)
    answer = []
    BFS(V)
    print(*answer, sep=' ')


def boj2606():
    V = int(input())
    E = int(input())
    visited = [False]*(V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    count = 0
    queue=deque([1])
    visited[1]=True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
                count+=1

    print(count)

# velog
def boj5567():
    V = int(input())
    E = int(input())
    visited = [0]*(V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    count = 0
    queue=deque([1])
    visited[1]=1
    while queue:
        v = queue.popleft()
        if visited[v]>2: break
        for i in graph[v]:
            if visited[i]==0:
                visited[i]=visited[v]+1
                queue.append(i)
                count+=1

    print(count)

# floyd
# https://whitehairhan.tistory.com/333
def boj11403():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for a in range(N):
            for b in range(N):
                # 현재 정점을 거치면 길이 있으면
                if graph[a][i]==1 and graph[i][b]==1:
                    graph[a][b]=1

    for row in graph:
        print(*row)

def boj11403_2():
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    def BFS(x):
        queue = deque([x])
        check = [0 for _ in range(N)] # 현재 정점과 연결 여부
        while queue:
            cur = queue.popleft()
            for i in range(N):
                if check[i]==0 and graph[cur][i]==1:
                    visited[x][i]=1
                    check[i] = 1
                    queue.append(i)

    for i in range(N):
        BFS(i)
    for row in graph:
        print(*row)


# *
def boj2660():

    def BFS(start):
        queue=deque([start])
        visited[start]=1
        while queue:
            v = queue.popleft()
            for i in graph[v]:
                if visited[i]==0:
                    visited[i]=visited[v]+1
                    queue.append(i)
        return max(visited)-1 # 시작이 1이므로 -1

    V = int(input())
    graph = [[] for _ in range(V + 1)]
    while True:
        u, v = map(int, input().split())
        if u == -1: break
        graph[u].append(v)
        graph[v].append(u)

    answer = { i:0 for i in range(1,V+1) } # 멤버별 점수 딕셔너리
    for i in range(1, V+1):
        visited = [0]*(V+1)
        answer[i] = BFS(i)

    arr = [] # 최소 점수를 가진 멤버 리스트
    for key, value in answer.items():
        if value == min(answer.values()):
            arr.append(key)
    print(min(answer.values()), len(arr))
    print(*sorted(arr))


if __name__=='__main__':
    boj11403()