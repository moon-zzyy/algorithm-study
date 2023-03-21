import sys
input = sys.stdin.readline


def boj1463():
    N = int(input())
    dp = [0] * (N + 1)  # 1~N 사용

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        if i % 2 == 0: dp[i] = min(dp[i], dp[i // 2] + 1)
        if i % 3 == 0: dp[i] = min(dp[i], dp[i // 3] + 1)
    print(dp[N])


def boj9095():
    dp = [0] * (10 + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 10 + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(dp[N])


# velog
def boj2579():
    N = int(input())
    arr = [0]
    for _ in range(N):
        arr.append(int(input()))
    if N < 3:  # 계단개수 2개 이하
        print(sum(arr))
        exit(0)

    dp = [0] * (N + 1)  # 밟지 않을 계단 점수의 최솟값
    for i in range(1, 4):  # index: 1,2,3 초기값 설정
        dp[i] = arr[i]

    for i in range(4, N):
        dp[i] = min(dp[i - 2], dp[i - 3]) + arr[i]

    print(sum(arr) - min(dp[N - 1], dp[N - 2]))


def boj1149():
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(N)]
    for i in range(1, N):
        dp[i][0] += min(dp[i - 1][1], dp[i - 1][2])  # R
        dp[i][1] += min(dp[i - 1][0], dp[i - 1][2])  # G
        dp[i][2] += min(dp[i - 1][0], dp[i - 1][1])  # B

    print(min(dp[N - 1]))  # 마지막 줄 집의 최솟값


def boj11726():
    N = int(input())
    if N < 3:
        print(N)
        exit(0)
    dp = [0, 1, 2]
    for i in range(3, N + 1):
        dp.append((dp[i - 2] + dp[i - 1]) % 10007)
    print(dp[N])


# prefix sum
def boj11659():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = [0]  # 누적 합
    temp = 0
    for n in arr:
        temp += n
        dp.append(temp)
    for _ in range(M):
        i, j = map(int, input().split())
        print(dp[j] - dp[i - 1])


# velog
def boj12852():
    N = int(input())
    dp = [0] * (N + 1)  # 횟수의 최솟값
    pre = [0] * (N + 1)  # 최소 경로
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        pre[i] = i - 1
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1
            pre[i] = i // 2
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
            pre[i] = i // 3
    print(dp[N])

    now = N
    while True:
        print(now, end=' ')
        if now == 1: break
        now = pre[now]


def boj1003():
    dp = [[0]] * 41
    dp[0] = [1, 0]
    dp[1] = [0, 1]
    for i in range(2, 41):
        x, y = dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]
        dp[i] = [x, y]
    for _ in range(int(input())):
        N = int(input())
        print(dp[N][0], dp[N][1])


def boj1932():
    N = int(input())
    dp = [list(map(int, input().split())) for _ in range(N)]

    for i in range(1, N):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] += dp[i - 1][j]
            elif j == i:
                dp[i][j] += dp[i - 1][j - 1]
            else:
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
    print(max(dp[N - 1]))


# velog
def boj11727():
    N = int(input())
    dp = [0, 1, 3]

    for i in range(3, N + 1):
        # dp.append((dp[i-2]*2 + dp[i-1]) % 10007)
        if i % 2 == 0:
            dp.append((dp[i - 1] * 2 + 1) % 10007)
        else:
            dp.append((dp[i - 1] * 2 - 1) % 10007)

    print(dp[N])


def boj2193():
    N = int(input())
    dp = [0, 1, 1]
    for i in range(3, N + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    print(dp[N])


# *
def boj1912():
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0]]
    for i in range(1, N):  # 직전원소와 합한 값, 새로 시작 중 큰 값
        dp.append(max(dp[i - 1] + arr[i]), arr[i])
    print(max(dp))

# *
# 참고: https://cotak.tistory.com/46
def boj11055():
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [arr[0]] # i번째까지 부분수열의 최대값
    for i in range(1, N): # i번째 미만 j번째 원소와 비교
        dp.append(arr[i])
        for j in range(i):
            if arr[j] < arr[i]:# 현재 원소보다 작으면
                dp[i] = max(dp[j]+arr[i],dp[i]) # 현재 값과 이전 값+현재 원소 비교
    print(max(dp))

# 참고: https://thingjin.tistory.com/entry/%EB%B0%B1%EC%A4%80-11053%EB%B2%88-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC
def boj11053():
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1]*N
    for i in range(1, N):
        for j in range(i):
            if arr[j]<arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))


def boj9461():
    dp = [0, 1, 1, 1, 2]
    for i in range(5, 101):
        dp.append(dp[i-2] + dp[i-3])

    for _ in range(int(input())):
        N = int(input())
        print(dp[N])

# velog
def boj14501():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    dp = [0]*(N+1)
    for i in range(N-1, -1, -1):
        t, p = arr[i]
        if i+t > N: # 퇴사일 이후
            dp[i] = dp[i+1]
        else: # 현재+1, 현재금액+현재시간이후금액
            dp[i] = max(dp[i+1], p+dp[i+t])

    print(dp[0])


# velog 위와 같은 답
def boj15486():
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    dp = [0] * (N + 1)
    for i in range(N - 1, -1, -1):
        t, p = arr[i]
        if i + t > N:  # 퇴사일 이후
            dp[i] = dp[i + 1]
        else:  # 현재+1, 현재금액+현재시간이후금액
            dp[i] = max(dp[i + 1], p + dp[i + t])

    print(dp[0])

# 참고: https://pacific-ocean.tistory.com/151
# dp[자릿수][1의자리]
def boj15486():
    N = int(input())
    dp = [[0]*10 for _ in range(N+1)]
    for j in range(1, 10):
        dp[1][j]=1
    for i in range(2, N+1):
        for j in range(10):
            if j==0:
                dp[i][j]=dp[i-1][1]
            elif j==9:
                dp[i][j]=dp[i-1][8]
            else:
                dp[i][j]=dp[i-1][j-1]+dp[i-1][j+1]
    print(sum(dp[N])%1000000000)


if __name__ == '__main__':
    boj14501()
