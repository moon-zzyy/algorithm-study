def q10871():
    N, X = map(int, input().split())
    arr = list(map(int, input().split()))

    for n in arr:
        if n < X:
            print(n, end=' ')


def q2562():
    arr = [int(input()) for _ in range(9)]

    print(max(arr))
    print(arr.index(max(arr)) + 1)


def q2587():
    arr = [int(input()) for _ in range(5)]
    arr.sort()

    print(sum(arr) // 5)
    print(arr[2])


# *
def q10093():
    A, B = map(int, input().split())
    A, B = min(A, B), max(A, B)
    d = B - A - 1
    if A == B:
        d = 0
    print(d)
    for n in range(A + 1, B):
        print(n, end=' ')


# *
def q2309():
    N = 9
    arr = [int(input()) for _ in range(N)]
    arr.sort()
    res = sum(arr)
    for i in range(N):
        for j in range(i + 1, N):
            if res - arr[i] - arr[j] == 100:
                for k in range(N):
                    if k!=i and k!=j:
                        print(arr[k])
                exit()


import itertools

def q2309_2():
    arr = [int(input()) for _ in range(9)]
    for n in itertools.combinations(arr, 7):
        if sum(n) == 100:
            for m in sorted(arr):
                print(m)
            break


if __name__ == '__main__':
    q2309_2()
