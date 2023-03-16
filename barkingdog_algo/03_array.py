import sys
input = sys.stdin.readline

def boj10808():
    S = input()
    arr = [0] *26
    for s in S:
        arr[ord(s)-ord('a')]+=1
    print(*arr, sep=' ')


def boj3273():
    N = int(input())
    arr = list(map(int, input().split()))
    X = int(input())
    nums = [0]*X
    answer=0
    for n in arr:
        if X-n > 0 and nums[X-n]: answer+=1
        if n<X: nums[n] = 1

    print(answer)


if __name__ == '__main__':
    boj3273()