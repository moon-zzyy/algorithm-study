import sys
input = sys.stdin.readline


def boj11047():
    N, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    answer=0
    for i in range(N-1, -1, -1):
        if K==0: break
        answer+= K//arr[i]
        K%=arr[i]

    print(answer)


def boj1931():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:(x[1],x[0]))

    time = 0
    answer = 0
    for start, end in arr:
        if time<=start:
            time=end
            answer+=1
    print(answer)

# *
def boj2217():
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    arr.sort(reverse=True)

    answer=0
    for i in range(N):
        answer = max(answer, arr[i]*(i+1))
    print(answer)


def boj1026():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()
    B.sort(reverse=True)
    answer=0
    for a, b in zip(A,B):
        answer+=a*b
    print(answer)


if __name__=='__main__':
    boj1026()