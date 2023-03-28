import bisect
import sys
input = sys.stdin.readline


def boj1920():
    def search(target):
        s, e = 0, N-1
        while s<=e:
            mid = (s+e)//2
            if arr[mid]>target:
                e = mid-1
            elif arr[mid] < target:
                s = mid+1
            else:
                return 1
        return 0 # s>e

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    M = int(input())
    for target in map(int,input().split()):
        print(search(target))

# velog
def boj10816():
    # def search(target):
    #     s, e = 0, N-1
    #     while s<=e:
    #         mid = (s+e)//2
    #         if arr[mid]>target:
    #             e = mid-1
    #         elif arr[mid] < target:
    #             s = mid+1
    #         else:
    #             return count[target]
    #     return 0 # s>e

    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    M = int(input())

    # count = {}
    # for i in arr:
    #     if i in count: count[i]+=1
    #     else: count[i]=1

    for target in map(int, input().split()):
        print(bisect.bisect_right(arr, target) - bisect.bisect_left(arr, target), end=' ')

# velog
def boj18870():
    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(set(arr))
    for target in arr:
        print(bisect.bisect_left(sorted_arr,target), end=' ')


def boj18870_2():
    def lower_bound(target,l):
        s, e = 0, l
        while s<e:
            mid = (s+e)//2
            if sorted_arr[mid]<target:
                s=mid+1
            else: e=mid
        return s # index

    N = int(input())
    arr = list(map(int, input().split()))
    sorted_arr = sorted(set(arr))
    for target in arr:
        print(lower_bound(target, len(sorted_arr)), end=' ')

# *
# 참고: https://2hs-rti.tistory.com/entry/%EB%B0%B1%EC%A4%80-2295%EB%B2%88-%EC%84%B8-%EC%88%98%EC%9D%98-%ED%95%A9-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# x+y+z=k -> x+y=k-z
# set 은 해시 테이블 존재하여 in 시간복잡도: O(1)
def boj2295():
    N = int(input())
    U = [int(input()) for _ in range(N)]
    U.sort()
    x_y_arr= set()
    for x in U:
        for y in U:
            x_y_arr.add(x+y)

    for i in range(N-1,-1,-1):
        for j in range(i+1):
            if U[i]-U[j] in x_y_arr: # O(1)
                print(U[i])
                exit(0)

# *
# parametric search
def boj1654():
    def solve(x):
        count = 0
        for n in arr:
            count+=n//x
        return count>=N

    K, N = map(int, input().split())
    arr = [int(input()) for _ in range(K)]
    s, e = 0, max(arr)
    while s<e:
        mid = (s+e+1)//2
        if solve(mid): s=mid
        else: e=mid-1
    print(s)


# velog
# 이진, set/dict
def boj10815():
    N = int(input())
    arr = set(map(int,input().split()))
    M = int(input())
    for target in map(int,input().split()):
        if target in arr: # O(1)
            print(1,end=' ')
        else:
            print(0,end=' ')


def boj10815_2():
    N = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    M = int(input())
    for target in map(int,input().split()):
        s, e = 0, N-1
        exist = False
        while s<=e:
            mid = (s+e)//2
            if target < arr[mid]:
                e=mid-1
            elif target > arr[mid]:
                s=mid+1
            else:
                exist = True
                break
        print(1 if exist else 0)


def boj1822():
    N, M = map(int,input().split())
    A = set(map(int,input().split()))
    B = set(map(int,input().split()))
    arr = sorted(A-B) # set 정렬 후 list 리턴
    print(len(arr))
    print(' '.join(map(str,arr)))


if __name__=='__main__':
    boj1654()