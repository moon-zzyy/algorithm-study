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
    arr.sort(reverse=True) # 내림차순

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


def boj11399():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(1,N):
        arr[i]+=arr[i-1]
    print(sum(arr))

# *
# - 기준 split() 후 sum()을 이용하여 첫째원소 이후 모두 빼기
def boj1541():
    arr = input().strip().split('-')
    answer=sum(list(map(int, arr[0].split('+'))))
    for s in arr[1:]:
        answer-=sum(list(map(int, s.split('+'))))
    print(answer)

# *
def boj11501():
    for _ in range(int(input())):
        N = int(input())
        arr = list(map(int, input().split()))
        max_price = -1e9
        answer=0
        for i in range(N-1,-1,-1):
            diff = max_price-arr[i]
            if diff>0: # 최대값과 현재주가 차이가 양수
                answer+=diff
            else: # 현재주가 최대값 변경
                max_price = arr[i]
        print(answer)

# *
# 참고: https://jokerldg.github.io/algorithm/2021/03/15/number-tie.html
def boj1744():
    N = int(input())
    pos,neg = [], []
    answer=0
    for _ in range(N):
        num = int(input())
        if num==1: answer+=1 # 1 처리
        elif num>0: pos.append(num)
        else: neg.append(num)
    pos.sort() # 오름차순
    neg.sort(reverse=True) # 내림차순

    for i in range(len(pos)//2): # 큰순으로 곱하기
        x=pos.pop()
        y=pos.pop()
        answer+=x*y
    if pos: answer+=pos.pop() # 홀수인경우
    for i in range(len(neg)//2): # 작은순으로 곱하기(음수*음수=양수)
        x=neg.pop()
        y=neg.pop()
        answer+=x*y
    if neg: answer+=neg.pop() # 홀수인경우

    print(answer)


if __name__=='__main__':
    boj13335()