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


if __name__=='__main__':
    boj18870()