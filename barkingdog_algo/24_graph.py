from collections import deque
import sys
input = sys.stdin.readline


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


if __name__=='__main__':
    boj1260()