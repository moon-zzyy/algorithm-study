import sys
input = sys.stdin.readline


# *
# 참고: https://jiwon-coding.tistory.com/21
def boj15649():
    def func():
        if len(arr) == M:  # 개수가 차면 출력 후 종료
            print(' '.join(map(str, arr)))
            return

        for i in range(1, N + 1):
            # if i not in arr:
            if not visited[i]:
                arr.append(i)
                visited[i] = True
                func()
                arr.pop()
                visited[i] = False

    N, M = map(int, input().split())
    arr = []  # 수열
    visited = [False] * (N + 1)
    func()


# *
# 참고: https://github.com/encrypted-def/basic-algo-lecture/blob/master/0x0C/solutions/9663.cpp
def boj9663():
    def func(cur):
        global count
        if cur == N:
            count += 1
            return

        for i in range(N):
            if visited1[i] or visited2[i + cur] or visited3[cur - i + N - 1]:
                continue
            visited1[i] = True
            visited2[i + cur] = True
            visited3[cur - i + N - 1] = True
            func(cur + 1)
            visited1[i] = False
            visited2[i + cur] = False
            visited3[cur - i + N - 1] = False

    N = int(input())
    visited1 = [False] * (N)
    visited2 = [False] * (2 * N - 1)
    visited3 = [False] * (2 * N - 1)

    func(0)
    print(count)


# *
# 참고: https://imzzan.tistory.com/151
def boj1182():
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))  # 부분수열

    def func(cur, total):
        global count
        if cur == N:  # N번 반복
            if total == S: count += 1
            return

        func(cur + 1, total)  # 포함 X
        func(cur + 1, total + arr[cur])  # 포함

    func(0, 0)
    print(count - 1 if S == 0 else count)  # 공집합 제외


def boj15649():
    def func():
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return

        for i in range(1, N + 1):
            if i not in arr:
                arr.append(i)
                func()
                arr.pop()

    N, M = map(int, input().split())
    arr = []
    func()


def boj15650():
    def func(start):
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return

        for i in range(start, N + 1):
            if i not in arr:
                arr.append(i)
                func(i + 1)
                arr.pop()

    N, M = map(int, input().split())
    arr = []
    func(1)


def boj15651():
    def func():
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return

        for i in range(1, N + 1):
            arr.append(i)
            func()
            arr.pop()

    N, M = map(int, input().split())
    arr = []
    func()


def boj15652():
    def func(start):
        if len(arr) == M:
            print(' '.join(map(str, arr)))
            return

        for i in range(start, N + 1):
            arr.append(i)
            func(i)
            arr.pop()

    N, M = map(int, input().split())
    arr = []
    func(1)

def boj15654():
    def func():
        if len(sequence)==M:
            print(' '.join(map(str,sequence)))
            return
        for i in range(N):
            if arr[i] not in sequence:
                sequence.append(arr[i])
                func()
                sequence.pop()

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    sequence =[]
    func()


def boj15655():
    def func(start):
        if len(sequence)==M:
            print(' '.join(map(str,sequence)))
            return
        for i in range(start,N):
            sequence.append(arr[i])
            func(i+1)
            sequence.pop()

    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    sequence =[]
    func(0)


def boj6603():
    def func(start):
        if len(lotto) == 6:
            print(' '.join(map(str, lotto)))
            return

        for i in range(start, K):
            if arr[i] not in lotto:
                lotto.append(arr[i])
                func(i + 1) # 현재 인덱스 다음부터 탐색가능
                lotto.pop()

    while True:
        arr = list(map(int, input().split()))
        K = arr[0] # 개수

        if K==0: exit() # 종료
        del arr[0]
        lotto = [] # 로또 당첨 번호
        func(0) # 시작인덱스
        print()


if __name__ == '__main__':
    count = 0
    boj15655()
