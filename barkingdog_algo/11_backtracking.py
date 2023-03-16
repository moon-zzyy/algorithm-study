import sys
input = sys.stdin.readline

# *
# 참고: https://jiwon-coding.tistory.com/21
def boj15649():
    def func():
        if len(arr)==M: # 개수가 차면 출력 후 종료
            print(' '.join(map(str,arr)))
            return

        for i in range(1,N+1):
            # if i not in arr:
            if not visited[i]:
                arr.append(i)
                visited[i]=True
                func()
                arr.pop()
                visited[i]=False

    N, M = map(int, input().split())
    arr = [] # 수열
    visited = [False]*(N+1)
    func()

# *
# 참고: https://github.com/encrypted-def/basic-algo-lecture/blob/master/0x0C/solutions/9663.cpp
def boj9663():
    def func(cur):
        global count
        if cur==N:
            count+=1
            return

        for i in range(N):
            if visited1[i] or visited2[i+cur] or visited3[cur-i+N-1]:
                continue
            visited1[i]=True
            visited2[i+cur]=True
            visited3[cur-i+N-1]=True
            func(cur+1)
            visited1[i]=False
            visited2[i+cur]=False
            visited3[cur-i+N-1]=False

    N = int(input())
    visited1=[False]*(N)
    visited2=[False]*(2*N-1)
    visited3=[False]*(2*N-1)

    func(0)
    print(count)

# *
# 참고: https://imzzan.tistory.com/151
def boj1182():
    N, S = map(int, input().split())
    arr = list(map(int, input().split())) # 부분수열

    def func(cur, total):
        global count
        if cur==N: # N번 반복
            if total==S: count+=1
            return

        func(cur+1, total) # 포함 X
        func(cur+1, total+arr[cur]) # 포함

    func(0,0)
    print(count-1 if S==0 else count) # 공집합 제외


if __name__ == '__main__':
    count = 0
    boj9663()